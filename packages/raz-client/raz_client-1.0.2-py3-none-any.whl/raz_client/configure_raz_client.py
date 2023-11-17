# Copyright (c) 2023 Cloudera, Inc.  All Rights Reserved.
# This software and any associated use of this software is governed exclusively
# by the Cloudera Standard License included in the accompanying LICENSE.txt file or found at
# https://www.cloudera.com/legal/terms-and-conditions/cloudera-standard-license/cloudera-standard-license-v9-2019-12-12.html.

"""Configures a boto3 client to be used with the RAZ server."""
import os.path

import raz_client
from raz_client import SSL_CERT_LOCATION, USE_SSL_VERIFICATION
from raz_client.raz_signer import RazS3Signer

CORE_FILE = "/etc/hadoop/conf/core-site.xml";


def configure_ranger_raz(botoclient, conf=None, ssl_file=None):
    """configures a boto3 client"""

    if not raz_client.raz_util.has_valid_kerberos_ticket():
        raise ConnectionError("No valid kerberos ticket found. Signer is not initialized")

    if conf is None:
        conf = raz_client.Configuration()
        file_exists = os.path.exists(CORE_FILE)
        if file_exists:
            conf.load_xml_file(CORE_FILE)

    if ssl_file is not None:
        conf[SSL_CERT_LOCATION] = ssl_file;
        conf[USE_SSL_VERIFICATION] = True

    botoclient.meta.events.register_first("choose-signer", raz_client.raz_util.return_signer)
    signer = RazS3Signer(conf)
    botoclient.meta.events.register("request-created", signer.sign)
