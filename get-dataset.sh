#! /bin/bash

sudo apt-get update
echo y | sudo apt-get install pip
sudo apt-get install python3
pip -q install sagemaker --upgrade
sudo apt-get -y install unzip

wget -N https://sagemaker-sample-data-us-west-2.s3-us-west-2.amazonaws.com/autopilot/direct_marketing/bank-additional.zip
unzip -o bank-additional.zip
