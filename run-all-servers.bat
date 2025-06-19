@echo off
cd /d "%~dp0"
start "RedirectServer" /min py -3 -m http.server 8000
start "SpotifyProxy"  /min "%~dp0run-proxy-py.bat"
exit

