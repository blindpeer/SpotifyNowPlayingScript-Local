@echo off
cd /d "%~dp0"

REM 1) Stage updated index.html
git add index.html

REM 2) Commit with message
git commit -m "docs: update Pages landing page to v1.5"

REM 3) Push to GitHub
git push origin main

pause
