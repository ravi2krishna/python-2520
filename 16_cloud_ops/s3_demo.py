# Using Boto3 SDK 
# Working with Different AWS Cloud API Resources 

import boto3

s3_client = boto3.client('s3')
# Listed Buckets 
response = s3_client.list_buckets()
print(response)

try:
# Create Bucket 
    response = s3_client.create_bucket(
        Bucket='python-2520-new',
        CreateBucketConfiguration={
            'LocationConstraint': 'us-east-2',
        },
    )
    print("Bucket Created",response )
except Exception as e:
    print("Error Creating Bucket: ",e)
    
# Upload Object 
# Define your bucket name, S3 object key, and local file path
bucket_name = 'python-2520-new'
s3_object_key = 'file.txt'
local_file_path = '16_cloud_ops/file.txt'

try:
    # Open the local file in binary read mode
    with open(local_file_path, 'rb') as f:
        # Upload the file content to S3 using put_object
        s3_client.put_object(Bucket=bucket_name, Key=s3_object_key, Body=f)
    print(f"File '{local_file_path}' uploaded successfully to '{s3_object_key}' in bucket '{bucket_name}'.")
except FileNotFoundError:
    print(f"Error: Local file '{local_file_path}' not found.")
except Exception as e:
    print(f"An error occurred during upload: {e}")
    
print(response)

# Delete Object 
try:
    # Delete the object
    response = s3_client.delete_object(Bucket=bucket_name, Key=s3_object_key)
    print(f"Object '{s3_object_key}' deleted successfully from bucket '{bucket_name}'.")
    # You can inspect the response for more details, e.g., response['DeleteMarker']
except Exception as e:
    print(f"Error deleting object '{s3_object_key}': {e}")

# Delete Bucket 
response = s3_client.delete_bucket(
    Bucket='python-2520-new',
)
