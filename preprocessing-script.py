#!/usr/bin/python3
from sagemaker.sklearn.processing import SKLearnProcessor

from sagemaker.processing import ProcessingInput, ProcessingOutput

import sagemaker

role = sagemaker.get_execution_role()

sklearn_processor = SKLearnProcessor(framework_version='0.23-1',
                                     role=role,
                                     instance_type='ml.c4.2xlarge',
                                     instance_count=1)

sklearn_processor.run(code='s3b.py',
                      inputs=[ProcessingInput(
                        source=input_data,
                        destination='bank-additional/bank-additional-full.csv')],
                      outputs=[ProcessingOutput(output_name='train_data',
                                                source='/opt/ml/processing/train/out-data2022-12-29 12:51:45'),
                               ProcessingOutput(output_name='test_data',
                                                source='/opt/ml/processing/test/out-data2022-12-29 12:51:45')],
                      arguments=['--train-test-split-ratio', '0.2']
                     )
