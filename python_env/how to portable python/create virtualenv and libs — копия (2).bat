"python-3.14.2-embed-amd64/python.exe" -m virtualenv "testing libraries +1/.venv"
CALL "testing libraries +1/.venv/Scripts/activate.bat"
pip freeze > "testing libraries +1/.venv/Scripts/requirements.txt"
exit
pip install -r "testing libraries/requirements.txt"
pip list

pause

