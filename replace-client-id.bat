@echo off
setlocal ENABLEDELAYEDEXPANSION

REM 1) Go to repo root
cd /d "%~dp0"

REM 2) Define your real ID and the placeholder
set "REAL_ID=YOUR_SPOTIFY_CLIENT_ID"
set "PLACEHOLDER=YOUR_SPOTIFY_CLIENT_ID"

echo Replacing %REAL_ID% with %PLACEHOLDER% in source files…

REM 3) Loop over relevant extensions
for %%F in (*.py *.html *.bat *.txt) do (
  if exist "%%F" (
    powershell -Command ^
      "(Get-Content -Raw '%%F') -replace '%REAL_ID%','%PLACEHOLDER%' | Set-Content '%%F'"
    echo  ✓ Updated %%F
  )
)

REM 4) Stage, commit & push
git add .
git commit -m "chore: replace hard-coded Client ID with placeholder"
git push origin main

echo.
echo ✅ Done! Your real Client ID has been scrubbed and replaced with a placeholder.
pause

