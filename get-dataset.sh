#! /bin/bash

sudo apt-get update
sudo apt-get install python3
sudo apt install python3-pip
pip3 install --upgrade setuptools wheel

pip3 install --upgrade setuptools wheel
python3 -m pip install s3fs --user
pip3 install boto3
#python3 -m pip install boto3 pandas s3fs --user
pip3 -q install sagemaker --upgrade
sudo apt-get -y install unzip
pip3 install scikit-learn

wget -N https://sagemaker-sample-data-us-west-2.s3-us-west-2.amazonaws.com/autopilot/direct_marketing/bank-additional.zip
unzip -o bank-additional.zip

mkdir -p /opt/ml/processing/train
mkdir -p /opt/ml/processing/test
mkdir -p /opt/ml/processing/input

cp bank-additional/bank-additional-full.csv /opt/ml/processing/input/
