# Copyright (c) 2023 Cloudera, Inc.  All Rights Reserved.
# This software and any associated use of this software is governed exclusively
# by the Cloudera Standard License included in the accompanying LICENSE.txt file or found at
# https://www.cloudera.com/legal/terms-and-conditions/cloudera-standard-license/cloudera-standard-license-v9-2019-12-12.html.

"""SSL usage example for the client"""

# for additional info on the params
# use: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#s3
import boto3

from raz_client import configure_ranger_raz
from raz_client import Configuration
from raz_client import RAZ_URL_KEY, SSL_CERT_LOCATION, USE_SSL_VERIFICATION

# configure the client
client = boto3.client("s3")
conf = Configuration()
conf[RAZ_URL_KEY] = "url of the raz server with port"
# enable ssl verification
conf[USE_SSL_VERIFICATION] = True
# add the cert location
conf[SSL_CERT_LOCATION] = "location of the cert file"
configure_ranger_raz(client, conf)

# uploading a file
client.upload_file("path/to/file.txt", "your-bucket", "path/to/key.txt")

# Downloading a file
client.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')
