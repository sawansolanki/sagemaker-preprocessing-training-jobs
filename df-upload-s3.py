import pandas as pd
import boto3
import datetime

bucket_name = "bkt-slp-slp"

datestring = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

client = boto3.client('s3')

response = client.put_object(
    Bucket='put-data-slp',
    Body='',
    Key=('opt/ml/processing/train/out-data-' + datestring + '/')
)

path = "s3://bkt-slp-psl/" + datestring +"/file.csv"

df = pd.read_csv('bank-additional/bank-additional-full.csv')

df.to_csv(path)
