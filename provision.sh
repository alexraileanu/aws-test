#!/usr/bin/env bash

sudo yum install -y git python3
git clone https://github.com/alexraileanu/aws-test $HOME/aws-test
cd $HOME/aws-test

virtualenv venv
pip install -r requirements.txt

sudo cp resources/api.service /lib/systemd/system/api.service
sudo systemctl daemon-reload
sudo systemctl start api.service