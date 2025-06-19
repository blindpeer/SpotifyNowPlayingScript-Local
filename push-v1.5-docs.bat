@echo off
REM push-v1.5-docs.bat — stage & push your v1.5 docs changes

:: 1) Ensure we’re in the repo root
cd /d "%~dp0"

:: 2) Pull latest from GitHub
echo Pulling latest from origin/main…
git pull origin main

:: 3) Stage only your updated docs
echo Staging docs/index.html and README.txt…
git add docs\index.html README.txt

:: 4) Commit with clear message
echo Committing…
git commit -m "docs: bump to v1.5 and add detailed landing page in docs/"

:: 5) Push back up
echo Pushing to origin/main…
git push origin main

echo.
echo ✅ Done — docs/index.html and README.txt v1.5 are now on GitHub!
pause
