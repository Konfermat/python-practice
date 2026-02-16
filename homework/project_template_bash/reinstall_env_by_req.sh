#!/bin/bash
cd "$(dirname "$0")"
rm -rf "../../.venv_ALT"
"../../../../.tools/python-3.14.2-embed-amd64/python.exe" -m virtualenv "../../.venv_ALT"
source "../../.venv_ALT/Scripts/activate"
python -m pip install -r "./requirements.txt"
read -n 1 -s -r -p "Press any key to continue..."