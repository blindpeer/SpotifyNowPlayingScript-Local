# Spotify NP Script (Local Edition)

## DESCRIPTION

**Spotify NP Script (Local Edition)** is a small, self-hosted tool that lets you post your current Spotify “Now Playing” into any chat client via a simple `/me` command.  
It uses a browser bookmarklet plus two lightweight local servers (an HTTP redirect page and a Flask proxy) to handle Spotify’s PKCE OAuth flow, token exchange, refresh, and throttling to prevent duplicate posts.

## HOW IT WORKS

1. **Installer prompts for your Spotify Client ID.**
   - **Press Enter to use the built-in default public Client ID** (recommended for most users).
2. **Generates all core files:**
   - `index.html`, `proxy.py`, `run-proxy-py.bat`, `run-all-servers.bat`, `bookmarklet.txt`
3. **Sets up a local Python virtual environment and installs Flask + dependencies.**
4. **Writes `bookmarklet.txt` containing the one-line bookmarklet.**
5. **Optionally starts the local servers immediately.**

---

## FEATURES

- One-click “Now Playing” `/me` message via browser bookmarklet  
- Secure PKCE authorization (no client secret needed/exposed)  
- Local Flask proxy for token and refresh exchanges (no public CORS proxy needed)  
- Automatic refresh-token support (no frequent re-authorization)  
- Persistent 5-second throttle to prevent flooding under lag  
- Customizable message format:  
  `/me is now playing: Artist – Track [Album] (https://open.spotify.com/…)`

---

## CONTENTS

After installation you will have:
- **index.html** – OAuth redirect callback page (http://127.0.0.1:8000)  
- **proxy.py** – Flask app (http://127.0.0.1:8888) for `/api/token` and `/api/refresh`  
- **run-proxy-py.bat** – Batch script to launch `proxy.py` inside a Python venv  
- **run-all-servers.bat** – Batch script to launch both servers  
- **bookmarklet.txt** – The one-line JavaScript bookmarklet  
- **venv/** – Python virtual environment with Flask, requests, flask-cors

---

## PREREQUISITES

- Windows 10 or 11  
- Python 3.7 or later on your PATH  
- **A Spotify app (Client ID only; no secret needed)**  
  - *If you don’t have one, just press Enter during setup to use the public default!*
  - Otherwise, create one here: https://developer.spotify.com/dashboard/create  
    - Add name and description for the app  
    - Add redirect URI: `http://127.0.0.1:8000/index.html`
- A chat client in the browser with a `cb().say(...)` API

---

## INSTALLATION

1. **Prepare an empty folder**, e.g.  
   `D:\Apps\SpotifyNP\`

2. **Copy these two installer files into that folder:**
   - `SpotifyNPScript-Local.py`
   - `Install_SpotifyNPScript-Local.bat`

3. *(Optional)* Open Command Prompt and `cd` into your folder:  
   `cd /d D:\Apps\SpotifyNP\`

4. **Run the installer:**  
   `Install_SpotifyNPScript-Local.bat`

5. **When prompted:**  
   - **To use your own Client ID:** Paste it and press Enter  
   - **To use the default public Client ID:** Just press Enter

6. The installer will:  
   - Write out all core files (`index.html`, `proxy.py`, batch scripts, `bookmarklet.txt`)  
   - Create a Python virtualenv (`venv\`) and install dependencies  
   - Ask “Start both servers now? (Y/N)” — answer **Y** to launch them immediately

---

## USAGE

1. **Ensure both servers are running** (HTTP on port 8000, proxy on port 8888).  
   - If you skipped “Y” at install, run:  
     `run-all-servers.bat`

2. **Install the bookmarklet:**  
   - Open `bookmarklet.txt`, copy its contents.  
   - Create a new browser bookmark and paste the string into its URL field.

3. **In any web page with `cb().say` available, click the bookmarklet.**
   - On first use, authorize Spotify in the popup.
   - Afterwards, it will post:  
     `/me is now playing: Artist – Track [Album] (https://open.spotify.com/…)`

---

## OPTIONAL: AUTO-START AT LOGIN

To have both servers start automatically whenever you log into Windows:

1. Open **Task Scheduler**
2. Create a new task triggered “At log on.”
3. **Action:** Start a program → `D:\Apps\SpotifyNP\run-all-servers.bat`
4. Check “Run only when user is logged on” and “Hidden.”
5. Save.

---

## SUPPORT & CUSTOMIZATION

- To change the chat message format, edit the `cb().say(...)` line in the bookmarklet.
- To add album art or auto-refresh at intervals, extend the bookmarklet or proxy code.
- For issues or questions, reach out to **blind_peer** @ GitHub.

---

**Enjoy seamless, flood-protected local “Now Playing” updates in your chat!**
