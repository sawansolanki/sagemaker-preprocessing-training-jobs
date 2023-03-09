#!/usr/bin/python3
from sagemaker.sklearn.estimator import SKLearn
import sagemaker
from sagemaker import get_execution_role
from time import gmtime, strftime
import boto3

#role = get_execution_role()
role='arn:aws:iam::256537223841:role/service-role/AmazonSageMaker-ExecutionRole-20221027T104692'

#output has been taken from "#running the processing job", this where it is defined
output = {'OutputName': 'test_data',
 'S3Output': {'S3Uri': 's3://sagemaker-us-east-1-256537223841/sagemaker-scikit-learn-2023-03-09-06-22-54-085/output/train_data',
  'LocalPath': '/opt/ml/processing/train',
  'S3UploadMode': 'EndOfJob'},
 'AppManaged': False}

preprocessed_training_data = output["S3Output"]["S3Uri"]
preprocessed_test_data = output["S3Output"]["S3Uri"]


def run_training():    
 
    sagemaker.Session(boto3.Session(region_name='us-east-1'))

    sklearn = SKLearn(
        entry_point="training.py", framework_version="0.20.0", instance_type="ml.c4.2xlarge", role=role
    )

    sklearn.fit({"train": preprocessed_training_data})
    training_job_description = sklearn.jobs[-1].describe()
    model_data_s3_uri = "{}{}/{}".format(
        training_job_description["OutputDataConfig"]["S3OutputPath"],
        training_job_description["TrainingJobName"],
        "output/model.tar.gz",
    )
    
    #endpoint_name = 'logistic-reg-endpoint'
    endpoint_name = 'logistic-regression-epc' + strftime("%Y-%m-%d-%H-%M-%S", gmtime())
    instance_type = 'ml.t2.medium'

    predictor = sklearn.deploy(
        initial_instance_count=1,
        instance_type=instance_type,
        endpoint_name=endpoint_name
    )
    
    
    
    #adding the endpoint part 
    #endpoint config
#     sm_client = boto3.client("sagemaker")
#     endpoint_config_name = 'xgboost-regression-epc' + strftime("%Y-%m-%d-%H-%M-%S", gmtime())
#     instance_type = "ml.c4.2xlarge"
#     print(endpoint_config_name)
#     create_endpoint_config_response = sm_client.create_endpoint_config(
#         EndpointConfigName = endpoint_config_name,
#         ProductionVariants=[{
#             'InstanceType': instance_type,
#             'InitialInstanceCount': 1,
#             'InitialVariantWeight': 1,
#             'ModelName': model,
#             'VariantName': 'AllTraffic'}])
#     print("Endpoint Configuration Arn: " + create_endpoint_config_response["EndpointConfigArn"])
    
#     #endpoint creation
    
#     endpoint_name = 'xgboost-realtime-ep' + strftime("%Y-%m-%d-%H-%M-%S", gmtime())
#     print("EndpointName={}".format(endpoint_name))

#     create_endpoint_response = sm_client.create_endpoint(
#         EndpointName=endpoint_name,
#         EndpointConfigName=endpoint_config_name)
#     print(create_endpoint_response['EndpointArn'])

#     # wait for endpoint to reach a terminal state (InService) using describe endpoint
#     import time

#     describe_endpoint_response = sm_client.describe_endpoint(EndpointName=endpoint_name)

#     while describe_endpoint_response["EndpointStatus"] == "Creating":
#         describe_endpoint_response = sm_client.describe_endpoint(EndpointName=endpoint_name)
#         print(describe_endpoint_response["EndpointStatus"])
#         time.sleep(15)

#     describe_endpoint_response

  


if __name__ == "__main__":
    run_training()
