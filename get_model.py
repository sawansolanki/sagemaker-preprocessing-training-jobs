import os
import boto3
import botocore
import joblib
s3 = boto3.resource('s3')

bucket_name = 'sagemaker-us-east-1-256537223841'
object_key = 'sagemaker-scikit-learn-2023-03-09-07-04-34-496/output/model.joblib'

# Extract the filename from the object key
filename = os.path.basename(object_key)

# Set local_file_path to the current working directory and the filename
local_file_path = os.path.join(os.getcwd(), filename)

try:
    s3.Bucket(bucket_name).download_file(object_key, local_file_path)
    joblib.load(local_file_path)
    print(f'Successfully downloaded file from S3 bucket {bucket_name} at object key {object_key} to {local_file_path}')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print(f"The object does not exist in bucket {bucket_name} at object key {object_key}")
    else:
        raise e
