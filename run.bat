@echo off
cd /d "%~dp0"

echo Activating virtual environment...
call venv\Scripts\activate

echo Running Job Application Automation CLI...
python app.py

echo.
echo Done. Press any key to close.
pause >nul
