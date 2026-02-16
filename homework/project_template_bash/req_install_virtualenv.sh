#!/bin/bash
cd "$(dirname "$0")"
source "../../.venv_ALT/Scripts/activate" 
python -m pip install -r "./requirements.txt"
#read -n 1 -s -r -p "Press any key to continue..."