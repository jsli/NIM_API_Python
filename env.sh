#!/bin/sh

# clean firstly
# rm .gitignore; rm -rf .git

# create virtual env for python
virtualenv --no-site-packages venv

# init virtual env
source venv/bin/activate

# install dependencies
pip install -r requirements.txt
