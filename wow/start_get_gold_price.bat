@echo off
cd /d "%~dp0"
:loop
python3 get_gold_price.py
timeout /t 1800 /nobreak >nul
goto loop