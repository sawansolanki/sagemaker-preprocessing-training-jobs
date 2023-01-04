#!/usr/bin/python3
import boto3
import sagemaker
from sagemaker import get_execution_role
from sagemaker.sklearn.processing import SKLearnProcessor
region = boto3.session.Session().region_name
from sagemaker.processing import ProcessingInput, ProcessingOutput

input_data = "s3://sagemaker-sample-data-{}/processing/census/census-income.csv".format(region)

def run_prepros():
#creating processing job instance
    #role = get_execution_role()
    role='arn:aws:iam::256537223841:role/service-role/AmazonSageMaker-ExecutionRole-20221027T104692'
    sklearn_processor = SKLearnProcessor(
        framework_version="0.20.0", role=role, instance_type="ml.c4.2xlarge", instance_count=1
    )

    sklearn_processor.run(
        code="preprocessing.py",
        inputs=[ProcessingInput(source=input_data, destination="/opt/ml/processing/input")],
        outputs=[
            ProcessingOutput(output_name="train_data", source="/opt/ml/processing/train"),
            ProcessingOutput(output_name="test_data", source="/opt/ml/processing/test"),
        ],
        arguments=["--train-test-split-ratio", "0.2"],
    )
    preprocessing_job_description = sklearn_processor.jobs[-1].describe()

    output_config = preprocessing_job_description["ProcessingOutputConfig"]
    for output in output_config["Outputs"]:
        if output["OutputName"] == "train_data":
            preprocessed_training_data = output["S3Output"]["S3Uri"]
        if output["OutputName"] == "test_data":
            preprocessed_test_data = output["S3Output"]["S3Uri"]
    
if __name__ == "__main__":
    run_prepros()
