@echo off
SETLOCAL EnableDelayedExpansion

REM 1) Ensure we’re in the repo root
cd /d "%~dp0"

REM 2) Pull & rebase remote changes
echo Pulling & rebasing from origin/main…
git pull --rebase origin main

if errorlevel 1 (
  echo.
  echo ERROR: rebase failed. Resolve conflicts, then re-run this script.
  pause
  exit /b 1
)

REM 3) Remove the accidental TEST directory (if it exists)
if exist TEST (
  echo Removing TEST/…
  git rm -r --ignore-unmatch TEST
)

REM 4) Stage only the core v1.5 files
echo Staging core v1.5 files…
git reset
git add index.html
git add proxy.py
git add run-proxy-py.bat
git add run-all-servers.bat
git add bookmarklet.txt
git add SpotifyNPScript-Local.py
git add Install_SpotifyNPScript-Local.bat
git add README.md
git add .gitignore

REM 5) Commit & push
echo Committing and pushing…
git commit -m "chore: clean repo & restore v1.5 landing page"
git push origin main

if errorlevel 1 (
  echo.
  echo ERROR: push failed. Check your network/auth, then re-run this script.
  pause
  exit /b 1
)

echo.
echo ✅ Clean v1.5 state pushed to GitHub!
pause
