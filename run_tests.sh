#!/bin/bash

# expects pip and python to match to pip3 and python3

echo 'Install dependencies'
pip install -r requirements.txt
echo 'Run tests'
python run.py
echo 'Done'
