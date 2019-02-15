#!/usr/bin/env bash

sudo yum install -y git python3 python3-devel gcc
sudo amazon-linux-extras install -y nginx1.12

git clone https://github.com/alexraileanu/aws-test $HOME/aws-test
cd $HOME/aws-test

sudo pip3.7 install virtualenv

virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

sudo cp resources/api.conf /etc/nginx/conf.d/api.conf
sudo systemctl restart nginx

sudo cp resources/api.service /lib/systemd/system/api.service
sudo systemctl daemon-reload
sudo systemctl start api.service
