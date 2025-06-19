@echo off
REM push-bookmarklet-update.bat — push bookmarklet + README changes to GitHub

:: 1) Ensure we’re in the repo root
cd /d "%~dp0"

:: 2) Grab the latest from upstream
echo Pulling latest from origin/main…
git pull origin main

:: 3) Keep readme.txt in sync with README.md (for GitHub page)
echo Syncing readme.txt → README.md…
copy /Y readme.txt README.md >nul

:: 4) Stage the updated files
echo Staging bookmarklet.txt and README.md…
git add bookmarklet.txt README.md

:: 5) Commit your updates
echo Committing…
git commit -m "chore: update bookmarklet to latest v1.5 lock version; sync README"

:: 6) Push up to GitHub
echo Pushing to origin/main…
git push origin main

echo.
echo ✅ bookmarklet.txt and README.md v1.5 have been pushed!
pause
