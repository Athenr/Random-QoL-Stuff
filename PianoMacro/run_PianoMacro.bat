@echo off

:: Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python first.
    pause
    exit /b
)

:: Install required module(s)
python -m pip install --upgrade pip
python -m pip install -r req_PianoMacro.txt

:: Run the Python script
python PianoMacro.py

pause