@echo off
cd /d "%~dp0"

REM Force Git to accept your local readme.txt, then push everything
git fetch origin main
git reset --hard origin/main
git add readme.txt bookmarklet.txt
git commit -m "chore: update bookmarklet + bump README to v1.5"
git push -u origin main --force

pause

