# Copyright (c) 2023 Cloudera, Inc.  All Rights Reserved.
# This software and any associated use of this software is governed exclusively
# by the Cloudera Standard License included in the accompanying LICENSE.txt file or found at
# https://www.cloudera.com/legal/terms-and-conditions/cloudera-standard-license/cloudera-standard-license-v9-2019-12-12.html.

"""Get Bucket Location Example"""

# for additional info on the params
# use: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#s3
import boto3

from raz_client import configure_ranger_raz
from raz_client import Configuration
from raz_client import RAZ_URL_KEY

# configure the client
client = boto3.client("s3")
conf = Configuration()
conf[RAZ_URL_KEY] = "url of the raz server with port"
configure_ranger_raz(client, conf)

# get bucket location
client.get_bucket_location(Bucket="BUCKET_NAME")
