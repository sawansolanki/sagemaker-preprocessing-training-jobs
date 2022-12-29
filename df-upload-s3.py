#!/usr/bin/python3
import pandas as pd
import boto3
import datetime

bucket_name = "bkt-slp-psl"

datestring = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

client = boto3.client('s3')

dpath = 'opt/ml/processing/train/out-data-' + datestring + '/'

response = client.put_object(
    Bucket='bkt-slp-psl',
    Body='',
    Key=(dpath))

path = "s3://bkt-slp-psl/opt/ml/processing/train/out-data-" + datestring +"/file.csv"

df = pd.read_csv('bank-additional/bank-additional-full.csv')

df.to_csv(path)
