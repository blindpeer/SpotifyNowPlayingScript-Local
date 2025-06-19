@echo off
setlocal

 1) Ensure we’re in the repo root
cd d %~dp0

 2) Fetch & rebase so we don’t get non-fast-forward errors
echo — Fetching and rebasing from originmain …
git fetch origin main
git rebase originmain
if errorlevel 1 (
  echo.
  echo ERROR Could not rebase. Resolve conflicts, then rerun this script.
  pause
  exit b 1
)

 3) Sync your readme.txt → README.md
echo.
echo — Syncing readme.txt → README.md …
copy Y readme.txt README.md nul

 4) Stage exactly the files we care about
echo.
echo — Staging bookmarklet.txt & README.md …
git add bookmarklet.txt README.md

 5) Commit if there are real changes
echo.
git diff --cached --quiet
if errorlevel 1 (
  git commit -m chore update bookmarklet lock+throttle; bump README to v1.5
) else (
  echo No changes to commit.
)

 6) Push back up
echo.
echo — Pushing to originmain …
git push origin main

echo.
echo ✅ Done! Your bookmarklet and README are now live on GitHub.
pause
