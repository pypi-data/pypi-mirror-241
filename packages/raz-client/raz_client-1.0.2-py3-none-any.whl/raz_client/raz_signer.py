# Copyright (c) 2023 Cloudera, Inc.  All Rights Reserved.
# This software and any associated use of this software is governed exclusively
# by the Cloudera Standard License included in the accompanying LICENSE.txt file or found at
# https://www.cloudera.com/legal/terms-and-conditions/cloudera-standard-license/cloudera-standard-license-v9-2019-12-12.html.

import base64
import datetime
import json
import logging
import re
import socket
import urllib.parse
import uuid

import requests
from requests_kerberos import HTTPKerberosAuth, REQUIRED
from urllib3.exceptions import ConnectionError as ConnError

from raz_client import signer_protos_pb2
from raz_client.raz_util import sanitize_resource_path, RazUnauthorizedException, Configuration, \
    print_to_raz_logs, parse_url_for_signing
from raz_client.raz_constants import USE_SSL_VERIFICATION, RAZ_URL_KEY, RAZ_DELEGATION_TOKEN_VALIDITY, \
    SSL_CERT_LOCATION, RAZ_CLIENT_USE_DELEGATION_TOKEN, RAZ_CLIENT_ENABLE_DEBUG_MODE


class RazS3Signer:

    def __init__(self, conf=None, auth_type="KERBEROS"):
        self.service_params = {
            'endpoint_prefix': 's3',
            'service_name': 's3',
            'serviceType': 's3'
        }
        self._service = 's3'
        self._auth = HTTPKerberosAuth(mutual_authentication=REQUIRED)
        self.is_debug_enabled = False
        self._auth_type = auth_type
        self._conf = Configuration(conf)
        self._raz_token = None
        self._raz_token_creation_time = None
        # setting this to 15m here for default
        self._raz_token_expiry_limit = 15 * 60 if conf[RAZ_DELEGATION_TOKEN_VALIDITY] is None \
            else conf[RAZ_DELEGATION_TOKEN_VALIDITY]

        self.logger = logging.getLogger("raz_client_logger")

        # turn off the ssl verification of by default if unset
        if self._conf[USE_SSL_VERIFICATION] is None:
            self._conf[USE_SSL_VERIFICATION] = False

        if self._conf[RAZ_CLIENT_ENABLE_DEBUG_MODE] is not None:
            self.enable_debug_mode()

    def _create_delegation_token(self):
        """Get the delegation token from the RAZ Server."""
        if self._conf[RAZ_URL_KEY] is None:
            raise AttributeError("Raz Url is not set.")

        self.logger.info("Creating a new delegation token for the client.")

        for current_raz_url in self._conf[RAZ_URL_KEY].split(","):
            try:
                raz_server_port = urllib.parse.urlparse(current_raz_url).port
                ip = socket.gethostbyname(urllib.parse.urlparse(current_raz_url).hostname)
                GET_PARAMS = {
                    "op": "GETDELEGATIONTOKEN",
                    "service": "%s:%s" % (ip, raz_server_port),
                    "renewer": "raz_client_python"
                }
                r = requests.get(current_raz_url, GET_PARAMS, auth=self._auth,
                                 verify=self._conf[SSL_CERT_LOCATION]
                                 if self._conf[USE_SSL_VERIFICATION] else False)
                if r.status_code != 200:
                    raise RazUnauthorizedException("Could not fetch delegation token from the server.")
                raz_token = json.loads(r.text)['Token']['urlString']
                return raz_token
            except (ConnError, requests.exceptions.ConnectionError) as error:
                self.logger.debug("Failed to talk with RAZ URL:{}, Error:{}".format(current_raz_url, error))
        # Raise an error if none of the url work, and we are not able to fetch the delegation tokens.
        raise ConnectionRefusedError("Unable to talk to any provided RAZ Server URLS!!!!")

    def _get_or_renew_delegation_token(self):
        if self._raz_token is None:
            self._raz_token = self._create_delegation_token()
            self._raz_token_creation_time = datetime.datetime.now()
        elif (datetime.datetime.now() - self._raz_token_creation_time).seconds > self._raz_token_expiry_limit:
            self._raz_token = self._create_delegation_token()
            self._raz_token_creation_time = datetime.datetime.now()
        return

    def _make_s3_request(self, request_data, request_headers, method, params, headers, url_params, endpoint,
                         resource_path, data=None):

        # In GET operations with non-ascii chars, only the non-ascii part is URL encoded.
        # We need to unquote the path fully before making a signed request for RAZ.
        for key in url_params:
            url_params[key] = urllib.parse.unquote(url_params[key])

        allparams = [signer_protos_pb2.StringListStringMapProto(key=key, value=[val])
                     for key, val in url_params.items()]
        allparams.extend([signer_protos_pb2.StringListStringMapProto(key=key, value=[val])
                          for key, val in params.items()])
        headers = [signer_protos_pb2.StringStringMapProto(key=key, value=val)
                   for key, val in headers.items()]

        self.logger.debug(
            "Preparing sign request with "
            "http_method: {%s}, headers: {%s}, parameters: {%s}, endpoint: {%s}, resource_path: {%s}, "
            "content_to_sign: {%s}" %
            (method, headers, allparams, endpoint, resource_path, data)
        )

        if data is not None and not isinstance(data, bytes):
            data = data.encode()

        raz_req = signer_protos_pb2.SignRequestProto(
            endpoint_prefix=self.service_params['endpoint_prefix'],
            service_name=self.service_params['service_name'],
            endpoint=endpoint,
            http_method=method,
            headers=headers,
            parameters=allparams,
            resource_path=resource_path,
            content_to_sign=data,
            time_offset=0
        )
        raz_req_serialized = raz_req.SerializeToString()
        signed_request = base64.b64encode(raz_req_serialized).decode('utf-8')

        request_headers["Accept-Encoding"] = "gzip,deflate"
        request_data["context"] = {
            "S3_SIGN_REQUEST": signed_request
        }
        return request_headers, request_data

    def _parse_raz_response(self, raz_response):
        raz_response_json = raz_response.json()
        result = raz_response_json.get("operResult", False) and raz_response_json["operResult"]["result"]

        if result == "NOT_DETERMINED":
            msg = "Failure %s" % raz_response_json
            raise RazUnauthorizedException(msg)

        if result != "ALLOWED":
            msg = "Permission missing %s" % raz_response_json
            logging.debug(msg)
            raise RazUnauthorizedException(msg)

        if result == "ALLOWED":
            signed_response_data = raz_response_json["operResult"]["additionalInfo"]
            signed_response_result = signed_response_data["S3_SIGN_RESPONSE"]
            if signed_response_result is not None:
                raz_response_proto = signer_protos_pb2.SignResponseProto()
                signed_response = raz_response_proto.FromString(base64.b64decode(signed_response_result))
                self.logger.debug("Received signed Response {}".format(signed_response))
                if signed_response is not None:
                    ret = dict([(i.key, i.value) for i in signed_response.signer_generated_headers])
                    return ret

    def _generate_raz_server_api_url(self, current_raz_url):

        if current_raz_url.endswith("/"):
            current_raz_url = current_raz_url.rstrip("/")

        if self._conf[RAZ_CLIENT_USE_DELEGATION_TOKEN] is None:
            raz_url = "{}/api/authz/{}/access?AUTH_TYPE=KERBEROS".format(current_raz_url, self._service)
        else:
            self._get_or_renew_delegation_token()
            raz_url = "{}/api/authz/{}/access?delegation={}".format(current_raz_url, self._service,
                                                                    self._raz_token)

        return raz_url

    def _check_access(self, method, url, bucket_name=None, params=None, headers=None, data=None,
                      operation=None, resource_path=None):
        self.logger.debug("Check access: method {%s}, url {%s}, bucket_name {%s}, "
                          "params {%s}, headers {%s}, operation {%s}, resource_path {%s}"
                          % (method, url, bucket_name, params, headers, operation, resource_path))

        # verification checks on the configs provided for signing
        if self._conf[USE_SSL_VERIFICATION] and self._conf[SSL_CERT_LOCATION] is None:
            raise AttributeError("Raz SSL Cert location is not set")

        if self._conf[RAZ_URL_KEY] is None:
            raise AttributeError("Raz URL is not set")

        headers = headers if headers is not None else {}
        resource_path = sanitize_resource_path(resource_path)
        params = params if params is not None else {}
        path, url_params = parse_url_for_signing(url)

        try:
            client_ip = socket.gethostbyname(socket.gethostname())
        except Exception:
            client_ip = ""

        request_data = {
            "requestId": str(uuid.uuid4()),
            "serviceType": 's3',
            "serviceName": 'cm_s3',
            "user": "",
            "userGroups": [],
            "clientIpAddress": client_ip,
            "clientType": "",
            "clusterName": socket.gethostname(),
            "clusterType": "",
            "sessionId": "",
            "accessTime": "",
            "context": {},
            "operation": {"resource": {}, "action": operation}
        }
        request_headers = {"Content-Type": "application/json"}

        if bucket_name == "":
            # this is a list bucket call
            url = "https://s3.amazonaws.com:443"
        else:
            url = "https://{bucket}.s3.amazonaws.com:443".format(bucket=bucket_name)

        self.logger.debug("endpoint {} params {} headers {} url_params {} resource_path {}".format(
            url, params, headers, url_params, resource_path))

        # convert the s3 request to a proto request to be transferred over the wire
        request_headers, request_data = self._make_s3_request(request_data, request_headers, method,
                                                              params, headers, url_params, url,
                                                              resource_path, data=data)

        self.logger.debug(request_data)

        verify = self._conf[SSL_CERT_LOCATION] if \
            self._conf[USE_SSL_VERIFICATION] else False

        # make the request to raz server by iterating over the raz urls
        for current_raz_url in self._conf[RAZ_URL_KEY].split(","):
            self.logger.debug("Starting a new RAZ connection to:{}".format(current_raz_url))
            try:
                raz_url = self._generate_raz_server_api_url(current_raz_url)
                raz_response = requests.post(raz_url, headers=request_headers, json=request_data,
                                             verify=verify,
                                             auth=self._auth)

                self.logger.debug(raz_response.json())

                if raz_response.ok:
                    return self._parse_raz_response(raz_response)
                else:
                    raise ConnError("Unable to talk with RAZ URL {}".format(current_raz_url))

            except (ConnError, requests.exceptions.ConnectionError) as error:
                self.logger.warning("Failed to talk with RAZ URL:{}, Error:{}".format(current_raz_url, error))
                self.logger.debug("{}".format(error))

            except RazUnauthorizedException as error:
                raise error

            except Exception as error:
                self.logger.warning("Failed to talk with RAZ URL:{}, Error:{}".format(current_raz_url, error))

        raise ConnError("Failed to talk with all RAZ URLS!!!!!!!")

    def sign(self, **kwargs):
        request = kwargs["request"]
        self.logger.debug("Url:{} Headers:{} Method:{}".format(request.url, request.headers, request.method))
        url_reg_virtual = "(.*)\.s3\.amazonaws\.com\/(.*)"
        url_reg_host = "s3.amazonaws.com\/(.*)"
        parsed_url = urllib.parse.urlparse(request.url)

        url_to_match = parsed_url.netloc + parsed_url.path
        matched_url = re.match(url_reg_virtual, url_to_match)
        if matched_url is None:
            # might be host style access
            matched_url = re.match(url_reg_host, url_to_match)
            if matched_url.group(1) == "":
                # this is a list buckets request
                bucket_name = ""
                path = ""
            else:
                bucket_name = matched_url.group(1).split("/")[0]
                path = "/".join(matched_url.group(1).split("/")[1:])
        else:
            bucket_name = matched_url.group(1)
            path = matched_url.group(2)
        raz_headers = self._check_access(method=request.method, bucket_name=bucket_name,
                                         url=request.url, headers=request.headers,
                                         operation=kwargs["operation_name"], resource_path=path)

        for key in raz_headers:
            request.headers[key] = raz_headers[key]
        request.headers["Host"] = "{bucket}.s3.amazonaws.com".format(bucket=bucket_name)
        path = sanitize_resource_path(path)
        request.url = urllib.parse.urlunparse(
            ("https", request.headers["Host"] + ":443", path, "", parsed_url.query, ""))
        self.logger.debug("Url for the request to S3:{}".format(request.url))
        return

    def enable_debug_mode(self):
        import http.client as http_client
        http_client.HTTPConnection.debuglevel = 1
        http_client.print = print_to_raz_logs
        self.logger.setLevel(logging.DEBUG)
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True

    def disable_debug_mode(self):
        import http.client as http_client
        http_client.HTTPConnection.debuglevel = 0
        http_client.print = print
        self.logger.setLevel(logging.WARNING)
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.WARNING)
