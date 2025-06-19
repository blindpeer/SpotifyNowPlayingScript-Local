@echo off
cd /d "%~dp0"
if not exist venv\Scripts\activate.bat (
  py -3 -m venv venv
)
call venv\Scripts\activate.bat
pip install flask requests flask-cors >nul
python proxy.py
pause

