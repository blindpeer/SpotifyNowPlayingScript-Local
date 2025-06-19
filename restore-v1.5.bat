@echo off
REM ───────────────────────────────────────────────────────────
REM restore-v1.5.bat — reset remote, remove TEST/, restore index.html
REM ───────────────────────────────────────────────────────────

cd /d "%~dp0"

REM 1) Discard any local unstaged changes
echo Resetting local changes…
git reset --hard origin/main

REM 2) Remove accidental TEST directory (if present)
if exist TEST (
  echo Removing TEST/…
  git rm -r --ignore-unmatch TEST
)

REM 3) Copy your index.html into place
REM    (Make sure you have your corrected index.html next to this script)
echo Restoring landing page…
copy /Y index.html .

REM 4) Stage & commit only the core files
echo Staging core files…
git add index.html proxy.py run-proxy-py.bat run-all-servers.bat ^
        bookmarklet.txt SpotifyNPScript-Local.py Install_SpotifyNPScript-Local.bat ^
        README.md .gitignore

echo Committing…
git commit -m "docs: restore full v1.5 landing page and prune repo"

REM 5) Push back up to GitHub
echo Pushing to origin/main…
git push origin main --force

echo.
echo ✅ Done – your v1.5 landing page is live and TEST/ is removed.
pause

