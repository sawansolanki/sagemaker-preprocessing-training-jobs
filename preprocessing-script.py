import boto3
import sagemaker
from sagemaker import get_execution_role
from sagemaker.sklearn.processing import SKLearnProcessor
from sagemaker.processing import ProcessingInput, ProcessingOutput

if __name__ == "__main__":
    
    role = get_execution_role()
    region = boto3.session.Session().region_name
    
    sklearn_processor = SKLearnProcessor(
    framework_version="0.20.0", role=role, instance_type="ml.m5.xlarge", instance_count=1
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


