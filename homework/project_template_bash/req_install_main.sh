#!/bin/bash
cd "$(dirname "$0")"
"../../../../.tools/python-3.14.2-embed-amd64/python.exe" -m pip install -r "./requirements.txt"
#read -n 1 -s -r -p "Press any key to continue..."