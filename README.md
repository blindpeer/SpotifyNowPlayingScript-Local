Spotify NP Script (Local Edition) v1.6
===============

DESCRIPTION
-----------
Spotify NP Script (Local Edition) is a small, self-hosted tool that lets you post your current Spotify “Now Playing” into any chat client via a simple `/me` command. It uses a browser bookmarklet plus two lightweight local servers (an HTTP redirect page and a Flask proxy) to handle Spotify’s PKCE OAuth flow, token exchange, and silent refresh—now with built-in throttling to prevent duplicate posts under lag.

FEATURES
--------
• One-click “Now Playing” via a browser bookmarklet  
• Secure PKCE authorization (no client secret exposed)  
• Local Flask proxy for token and refresh exchanges (no public CORS proxy)  
• Automatic refresh-token support (no re-authorization every hour)  
• Persistent 5-second throttle to prevent flooding under lag  
• Customizable message format:  
    /me is now playing: Artist – Track [Album] (https://open.spotify.com/…)

CONTENTS
--------
After installation you will have:
  • index.html  
      – Landing page & OAuth redirect callback (served on http://127.0.0.1:8000)  
  • proxy.py  
      – Flask app (runs on http://127.0.0.1:8888) for /api/token and /api/refresh  
  • run-proxy-py.bat  
      – Batch script to launch proxy.py inside a Python venv  
  • run-all-servers.bat  
      – Batch script to launch both the HTTP server (8000) and the proxy (8888)  
  • bookmarklet.txt  
      – The one-line JavaScript bookmarklet you paste into your browser  
  • venv/  
      – Python virtual environment with Flask, requests, flask-cors  

PREREQUISITES
-------------
  • Windows 10 or 11  
  • Python 3.7 or later on your PATH  
  • A registered Spotify app (Client ID only; no secret needed)  
  • A chat client in the browser with a `cb().say(...)` API  

INSTALLATION
------------
1. Prepare an empty folder, e.g.  
     D:\Apps\SpotifyNP\  

2. Copy these two installer files into that folder:  
     • SpotifyNPScript-Local.py  
     • Install_SpotifyNPScript-Local.bat  

3. Open Command Prompt and `cd` into your folder:  
     cd /d D:\Apps\SpotifyNP\  

4. Run the installer:  
     Install_SpotifyNPScript-Local.bat  

5. When prompted, enter your **Spotify Client ID** and press Enter.  

6. The installer will:  
   - Write out index.html, proxy.py, run-proxy-py.bat, run-all-servers.bat, bookmarklet.txt  
   - Create a Python virtualenv (`venv\`) and install Flask + dependencies  
   - Ask “Start both servers now? (Y/N)” — answer **Y** to launch them immediately  

7. In your Spotify Developer Dashboard, add the redirect URI:  
     http://127.0.0.1:8000/index.html  

USAGE
-----
1. Ensure both servers are running (HTTP on port 8000, proxy on port 8888).  
   - If you skipped “Y” at install, run:  
       run-all-servers.bat  

2. Install the bookmarklet:  
   - Open bookmarklet.txt, copy its contents.  
   - Create a new browser bookmark and paste the string into its URL field.  

3. In any web page with `cb().say` available, click the bookmarklet.  
   - On first use, authorize Spotify in the popup.  
   - Afterwards, it will post:  
       /me is now playing: Artist – Track [Album] (https://open.spotify.com/…)  

OPTIONAL: AUTO-START AT LOGIN
-----------------------------
To have both servers start automatically whenever you log into Windows:

1. Open Task Scheduler.  
2. Create a new task triggered “At log on.”  
3. Action: Start a program → `D:\Apps\SpotifyNP\run-all-servers.bat`  
4. Check “Run only when user is logged on” and “Hidden.”  
5. Save.  

Now your local servers will always be ready.

CHANGELOG
---------
v1.6 (2025-06-19)
  • Dark-mode landing page with system-UI font, tighter spacing, styled ASCII header
  • Streamlined layout for headings, lists & code blocks
  • Robust bookmarklet guard: combined _invoked lock + persistent 5 s throttle
  • Version bump everywhere from v1.5 → v1.6
  • Docs refresh: full styled docs/index.html restored; README synced

SUPPORT & CUSTOMIZATION
-----------------------
• To change the chat message format, edit the `cb().say(...)` line in the bookmarklet.  
• To add album art or auto-refresh at intervals, extend the bookmarklet or proxy code.  
• For issues or questions, reach out to blind_peer  
    - blind_peer@protonmail.ch

Enjoy seamless, flood-protected local “Now Playing” updates in your chat!
