# Using Boto3 SDK 
# Working with Different AWS Cloud API Resources 

import boto3

s3_client = boto3.client('s3')
# Listed Buckets 
response = s3_client.list_buckets()
print(response)

# Create Bucket 
response = s3_client.create_bucket(
    Bucket='example-bucket',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2',
    },
)
print(response)

