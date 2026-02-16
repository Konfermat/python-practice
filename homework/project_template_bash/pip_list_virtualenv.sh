#!/bin/bash
cd "$(dirname "$0")"
source "../../.venv_ALT/Scripts/activate"
python -m pip list
read