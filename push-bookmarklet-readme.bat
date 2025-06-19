@echo off
REM push-bookmarklet-readme.bat — stage & push only the bookmarklet + README

cd /d "%~dp0"

echo === 1) Pull latest from origin/main ===
git pull origin main

echo.
echo === 2) Sync readme.txt → README.md ===
copy /Y readme.txt README.md >nul

echo.
echo === 3) Stage bookmarklet.txt & README.md ===
git add bookmarklet.txt README.md

echo.
echo === 4) Commit changes ===
git commit -m "chore: update bookmarklet throttle + sync README to v1.5"

echo.
echo === 5) Push to origin/main ===
git push origin main

echo.
echo ✅ Done! bookmarklet.txt and README.md are now up-to-date on GitHub.
pause

