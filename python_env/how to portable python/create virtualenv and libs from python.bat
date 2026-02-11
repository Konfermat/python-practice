"python-3.14.2-embed-amd64/python.exe" -m virtualenv "testing libraries/.venv"
"python-3.14.2-embed-amd64/python.exe" -m pip freeze > "testing libraries/requirements.txt"
"python-3.14.2-embed-amd64/python.exe" -m pip install -r "testing libraries/requirements.txt"
"python-3.14.2-embed-amd64/python.exe" -m pip list

pause

