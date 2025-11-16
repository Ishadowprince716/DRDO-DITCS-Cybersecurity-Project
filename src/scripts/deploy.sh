#!/bin/bash
# deploy.sh

# Script for deploying the DRDO DITCS cybersecurity system

pip install -r src/requirements.txt
python3 src/main.py
