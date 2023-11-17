# Copyright (c) 2023 Cloudera, Inc.  All Rights Reserved.
# This software and any associated use of this software is governed exclusively
# by the Cloudera Standard License included in the accompanying LICENSE.txt file or found at
# https://www.cloudera.com/legal/terms-and-conditions/cloudera-standard-license/cloudera-standard-license-v9-2019-12-12.html.

"""RAZ Client python package provides plugin to boto3 library to use
Apache Ranger for granular authorization for S3 access"""

from raz_client.raz_constants import USE_SSL_VERIFICATION, RAZ_URL_KEY, RAZ_DELEGATION_TOKEN_VALIDITY, \
    SSL_CERT_LOCATION, RAZ_CLIENT_USE_DELEGATION_TOKEN, RAZ_CLIENT_ENABLE_DEBUG_MODE
from raz_client.raz_util import Configuration, RazUnauthorizedException
from raz_client.configure_raz_client import configure_ranger_raz

__version__='1.0.2'
