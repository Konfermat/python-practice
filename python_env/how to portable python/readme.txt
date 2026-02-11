порядок установки:

Установи pip в python-3.14.2-embed-amd64
install pip.bat
После этого раскомментируйте строку import site в файле python3x._pth (или добавьте пути вручную), 
чтобы pip работал корректно.

Установи виртуальное окружение в python-3.14.2-embed-amd64
install virtualenv.bat

создай виртульное окружение в testing python-3.14.2-embed-amd64
create virtualenv.bat

для запуска файла testing python-3.14.2-embed-amd64/main.py через .venv
.venv launch main.bat

для запуска файла testing python-3.14.2-embed-amd64/main.py через .venv без активации (не тестил)
.venv launch main(ALT1).bat