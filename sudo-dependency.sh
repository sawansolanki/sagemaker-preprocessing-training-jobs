#! /bin/bash

sudo apt-get update
sudo apt-get -y install python3
sudo apt-get install python3-pip -y

pip3 install --upgrade setuptools wheel
python3 -m pip install s3fs --user
pip3 install boto3

python3 -m pip install boto3 pandas s3fs sagemaker --user
#pip3 -q install sagemaker --upgrade
sudo apt-get -y install unzip

pip3 install scikit-learn
#pip3 install sklearn
pip3 install argparse

# sudo curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
# sudo apt-get install less
# sudo unzip awscliv2.zip
# sudo ./aws/install

sudo apt-get install -y docker.io
sudo service docker start

sudo mkdir -p /opt/ml/processing/train
sudo mkdir -p /opt/ml/processing/test
sudo mkdir -p /opt/ml/processing/input

pip3 install awscli --upgrade --user 
pip3 install --upgrade boto3
