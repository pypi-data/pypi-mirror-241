# Copyright (c) 2023 Cloudera, Inc.  All Rights Reserved.
# This software and any associated use of this software is governed exclusively
# by the Cloudera Standard License included in the accompanying LICENSE.txt file or found at
# https://www.cloudera.com/legal/terms-and-conditions/cloudera-standard-license/cloudera-standard-license-v9-2019-12-12.html.

"""Utility methods for raz_client"""

import logging
import os
import re
import subprocess
import urllib
import xml.etree.ElementTree as ET
from urllib.parse import parse_qs

import botocore

path_normalize_regex = re.compile("/+")


def return_signer(**kwargs):
    """Returns a UNSIGNED signer type when called"""
    return botocore.UNSIGNED


def sanitize_resource_path(path):
    """Removes multiple / with a single occurrence to sanitize the path"""
    path = re.sub(path_normalize_regex, "/", path)
    if path.startswith("/"):
        path = path.lstrip("/")
    return path


def parse_url_for_signing(url):
    """Parses the given url and returns the path and the url params"""
    path = urllib.parse.urlparse(url)
    url_params = parse_qs(path.query, keep_blank_values=True)
    url_params = {
        key: url_params[key][0] for key in url_params
    }
    return path, url_params


def print_to_raz_logs(*args):
    """Configures the print, to print the HTTP debug to LOG"""
    logging.getLogger("raz_client_logger").debug(" ".join(args))


def has_valid_kerberos_ticket():
    """check is there is a valid kerberos ticket or not"""
    return True if subprocess.call(['klist', '-s']) == 0 else False


class RazUnauthorizedException(Exception):
    """Exception Class for AccessDenied on the RAZ Server calls"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Configuration:
    """Configuration class for raz client. The configs can be set in a dictionary manner."""

    def __init__(self, user_config=None):
        self.config_map = {}
        if user_config is not None:
            for key in user_config:
                self.config_map[key] = user_config[key]

    def __setitem__(self, key, value):
        self.config_map[key] = value

    def __getitem__(self, item):
        return self.config_map[item] if item in self.config_map else None

    def __len__(self):
        return len(self.config_map)

    def __iter__(self):
        return iter(self.config_map.keys())

    def load_xml_file(self, filename):
        if not os.path.exists(filename):
            raise FileNotFoundError("The XML file:{} does not exist.".format(filename))

        root = ET.parse(filename).getroot()
        for config_property in root.findall("property"):
            name = config_property.find("name").text
            value = config_property.find("value").text
            self.config_map[name] = value
