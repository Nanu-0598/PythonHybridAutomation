@echo off
call venv\scripts\activate
pytest -s -v -m "sanity" --html .\reports\report.html --browser chrome
pause
