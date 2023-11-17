# Copyright (c) 2023 Cloudera, Inc.  All Rights Reserved.
# This software and any associated use of this software is governed exclusively
# by the Cloudera Standard License included in the accompanying LICENSE.txt file or found at
# https://www.cloudera.com/legal/terms-and-conditions/cloudera-standard-license/cloudera-standard-license-v9-2019-12-12.html.

"""Delegation token example"""

# for additional info on the params
# use: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#s3
import boto3

from raz_client import configure_ranger_raz
from raz_client import Configuration
from raz_client import RAZ_URL_KEY, SSL_CERT_LOCATION, USE_SSL_VERIFICATION, \
    RAZ_CLIENT_USE_DELEGATION_TOKEN, RAZ_DELEGATION_TOKEN_VALIDITY

# configure the client
client = boto3.client("s3")
conf = Configuration()
conf[RAZ_URL_KEY] = "url of the raz server with port"
# enable ssl verification
conf[USE_SSL_VERIFICATION] = True
# add the cert location
conf[SSL_CERT_LOCATION] = "location of the cert file"
# enable delegation token on the client
conf[RAZ_CLIENT_USE_DELEGATION_TOKEN] = True
# the validity of the delegation token can be updated using the
# given param, the default is set to 15m
# setting it to 10s, any request made using DT will get the token renewed
conf[RAZ_DELEGATION_TOKEN_VALIDITY] = 10
configure_ranger_raz(client, conf)

# uploading a file
client.upload_file("path/to/file.txt", "your-bucket", "path/to/key.txt")

# Downloading a file
client.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')
