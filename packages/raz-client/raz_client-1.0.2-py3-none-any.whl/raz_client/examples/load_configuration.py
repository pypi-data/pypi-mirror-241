# Copyright (c) 2023 Cloudera, Inc.  All Rights Reserved.
# This software and any associated use of this software is governed exclusively
# by the Cloudera Standard License included in the accompanying LICENSE.txt file or found at
# https://www.cloudera.com/legal/terms-and-conditions/cloudera-standard-license/cloudera-standard-license-v9-2019-12-12.html.

"""Configuration load example from a static xml file"""

# for additional info on the params
# use: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#s3
import boto3

from raz_client import configure_ranger_raz
from raz_client import Configuration
from raz_client import RAZ_URL_KEY

# configure the client
client = boto3.client("s3")
conf = Configuration()
# load the hadoop configuration file
# Note: the configuration file expects the string values of the config
# rather than the variable names.
# the example file will look like this
# <configuration>
#     <property>
#             <name>fs.s3a.ext.raz.rest.host.url</name>
#             <value>full_raz_server_url</value>
#     </property>
#     <property>
#             <name>property_name_2</name>
#             <value>value_2</value>
#     </property>
# </configuration>
conf.load_xml_file("path to file")
# check for the raz server key
print(conf[RAZ_URL_KEY])
configure_ranger_raz(client, conf)

# uploading a file
client.upload_file("path/to/file.txt", "your-bucket", "path/to/key.txt")

# Downloading a file
client.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')
