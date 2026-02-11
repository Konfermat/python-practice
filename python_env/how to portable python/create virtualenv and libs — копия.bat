"python-3.14.2-embed-amd64/python.exe" -m virtualenv "testing libraries/.venv";
CALL "testing libraries/.venv/Scripts/activate.bat";
pip freeze > "testing libraries/requirements.txt";
pip install -r libraries/requirements.txt;
pip list
pause

REM CALL "testing libraries/.venv/Scripts/activate.bat";
REM pause
REM python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt
REM pip freeze > "testing libraries/requirements.txt"