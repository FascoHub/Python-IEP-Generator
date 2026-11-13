@echo off
REM Windows: creates a virtual environment on first run, then starts IEP Assist at http://localhost:8080
cd /d "%~dp0"
if not exist .venv ( py -m venv .venv && .venv\Scripts\pip install -r requirements.txt --quiet )
start "" http://localhost:8080
.venv\Scripts\python main.py
