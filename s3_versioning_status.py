# General Overview // Lambda - Py 3.8 , IAM to S3,versioning. 
# Can get the buckets with versioning enabled from list of buckets in specific account 


import json 
import boto3 
from botocore.exceptions import ClientError

def lambda_handler(event, context):
        s3 = boto3.client('s3')
        response = s3.list_buckets()
        for bucket in response["Buckets"]:
            try:
                response1 = s3.get_bucket_versioning(Bucket=bucket["Name"])
                if 'Status' in response1 and response1['Status'] == 'Enabled':
                    print(bucket["Name"])
            except:
                pass
