#! /bin/bash

sudo apt-get update
sudo apt-get install python3
sudo apt install python3-pip -y

pip3 install --upgrade setuptools wheel
python3 -m pip install s3fs --user
pip3 install boto3

python3 -m pip install boto3 pandas s3fs sagemaker --user
#pip3 -q install sagemaker --upgrade
sudo apt-get -y install unzip

pip3 install scikit-learn
wget -N https://sagemaker-sample-data-us-west-2.s3-us-west-2.amazonaws.com/autopilot/direct_marketing/bank-additional.zip
unzip -o bank-additional.zip

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo apt-get install less
unzip awscliv2.zip
sudo ./aws/install

sudo mkdir -p /opt/ml/processing/train
sudo mkdir -p /opt/ml/processing/test
sudo mkdir -p /opt/ml/processing/input
sudo mkdir -p /opt/ml/processing/input/code

cp preprocessing.py /opt/ml/processing/input/code/
cp bank-additional/bank-additional-full.csv /opt/ml/processing/input/
