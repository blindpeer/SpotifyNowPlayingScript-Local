@echo off
cd /d "%~dp0"

echo === 1) git pull ===
git pull origin main
if errorlevel 1 (
  echo ERROR: git pull failed. Check your network/auth and retry.
  pause
  exit /b 1
)

echo.
echo === 2) Sync readme.txt → README.md ===
copy /Y readme.txt README.md >nul

echo.
echo === 3) Stage bookmarklet.txt & README.md ===
git add bookmarklet.txt README.md

echo.
echo === 4) Commit if there are changes ===
git diff --cached --quiet
if errorlevel 1 (
  git commit -m "chore: update bookmarklet lock+throttle; bump README to v1.5"
) else (
  echo No changes to commit.
)

echo.
echo === 5) git push ===
git push origin main
if errorlevel 1 (
  echo ERROR: git push failed.  
) else (
  echo ✅ Pushed successfully.
)

pause

