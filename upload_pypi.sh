#!/bin/sh

python setup.py sdist

twine upload $1

