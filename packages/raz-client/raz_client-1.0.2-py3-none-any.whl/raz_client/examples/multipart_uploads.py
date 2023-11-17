# Copyright (c) 2023 Cloudera, Inc.  All Rights Reserved.
# This software and any associated use of this software is governed exclusively
# by the Cloudera Standard License included in the accompanying LICENSE.txt file or found at
# https://www.cloudera.com/legal/terms-and-conditions/cloudera-standard-license/cloudera-standard-license-v9-2019-12-12.html.

"""MultipartUpload example for the client"""

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

# create a multipart upload
response = client.create_multipart_upload(Bucket="BUCKET_NAME", Key="OBJECT_NAME")
upload_id = response["UploadId"]
# list the multipart uploads with a path
client.list_multipart_uploads(Bucket="BUCKET_NAME", Key="OBJECT_NAME")
# upload a part
part = client.upload_part(Bucket="BUCKET_NAME", Key="OBJECT_NAME", PartNumber=1, UploadId=upload_id,
                          Body="Body of the object")
part_info = {
    "Parts": [
        {
            "PartNumber": 1,
            "ETag": part["ETag"]
        }
    ]
}
client.list_parts(Bucket="BUCKET_NAME", Key="OBJECT_NAME", UploadId=upload_id)
# finish the upload
client.complete_multipart_upload(Bucket="BUCKET_NAME", Key="OBJECT_NAME",
                                 UploadId=upload_id, MultipartUpload=part_info)
