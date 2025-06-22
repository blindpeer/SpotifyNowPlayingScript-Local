# Spotify NP Script (Local Edition) v1.7

License: [PNC](LICENSE)
[![GitHub Pages](https://img.shields.io/badge/Docs-GitHub%20Pages-blue.svg)](https://blindpeer.github.io/SpotifyNowPlayingScript-Local/)

## Description

Spotify Now Playing Script (Local Edition) is a small, self-hosted tool that lets you post your current Spotify “Now Playing” into any chat client via a simple `/me` command. It uses a browser bookmarklet plus two lightweight local servers (an HTTP redirect page and a Flask proxy) to handle Spotify’s PKCE OAuth flow, token exchange, and silent refresh—now with built-in throttling to prevent duplicate posts under lag.

**What the script will do:**
1. Prompts for your Spotify Client ID.  
2. Generates the core files:
   - `index.html`  
   - `proxy.py`  
   - `run-proxy-py.bat`  
   - `run-all-servers.bat`  
   - `bookmarklet.txt`  
3. Creates a Python virtualenv (`venv`) and installs Flask + dependencies.  
4. Offers to start the local servers immediately.

## Features

- One-click “Now Playing” `/me` command via a browser bookmarklet  
- Secure PKCE authorization (no client secret exposed)  
- Local Flask proxy for token and refresh exchanges (no public CORS proxy)  
- Automatic refresh-token support (no re-authorization every hour)  
- Persistent 5 second throttle to prevent flooding under lag  
- Customizable message format:  
```
/me is now playing: Artist – Track [Album] (https://open.spotify.com/…)

```

## Contents

After installation you will have:
- **index.html**  
– Landing page & OAuth redirect callback (served on http://127.0.0.1:8000)  
- **proxy.py**  
– Flask app (runs on http://127.0.0.1:8888) for `/api/token` and `/api/refresh`  
- **run-proxy-py.bat**  
– Batch script to launch `proxy.py` inside a Python venv  
- **run-all-servers.bat**  
– Batch script to launch both the HTTP server (8000) and the proxy (8888)  
- **bookmarklet.txt**  
– The one-line JavaScript bookmarklet you paste into your browser  
- **venv/**  
– Python virtual environment with Flask, requests, flask-cors  

## Prerequisites

- Windows 10 or 11  
- Python 3.7 or later on your PATH  
- A registered Spotify app (Client ID only; no secret needed) in the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)  
- Add redirect URI: `http://127.0.0.1:8000/index.html`  
- A chat client in the browser with a `cb().say(...)` API  

## Installation

1. Prepare an empty folder, e.g.  
```

D:\Apps\SpotifyNP\\

````
2. Copy these two installer files into that folder:  
- `SpotifyNPScript-Local.py`  
- `Install_SpotifyNPScript-Local.bat`  
3. (Optional) Open Command Prompt and `cd` into your folder:  
```bat
cd /d D:\Apps\SpotifyNP\
````

4. Run the installer:

   ```bat
   Install_SpotifyNPScript-Local.bat
   ```
5. When prompted, enter your **Spotify Client ID** and press Enter.
6. The installer will:

   * Write out `index.html`, `proxy.py`, `run-proxy-py.bat`, `run-all-servers.bat`, `bookmarklet.txt`
   * Create a Python virtualenv (`venv\`) and install Flask + dependencies
   * Ask “Start both servers now? (Y/N)” — answer **Y** to launch them immediately

## Usage

1. Ensure both servers are running (HTTP on port 8000, proxy on port 8888).

   * If you skipped “Y” at install, run:

     ```bat
     run-all-servers.bat
     ```
2. Install the bookmarklet:

   * Open `bookmarklet.txt`, copy its contents.
   * Create a new browser bookmark and paste the string into its URL field.
3. In any web page with `cb().say` available, click the bookmarklet.

   * On first use, authorize Spotify in the popup.
   * Afterwards, each click posts:
     ```
     /me is now playing: Artist – Track [Album] (https://open.spotify.com/…)
     ```

## Optional: Auto-Start at Login

To have both servers start automatically whenever you log into Windows:

1. Open Task Scheduler.
2. Create a new task triggered “At log on.”
3. Action: Start a program → `D:\Apps\SpotifyNP\run-all-servers.bat`
4. Check “Run only when user is logged on” and “Hidden.”
5. Save.

## Quickstart (one-line)

```bash
git clone https://github.com/blindpeer/SpotifyNowPlayingScript-Local.git &&
cd SpotifyNowPlayingScript-Local &&
Install_SpotifyNPScript-Local.bat
```

## Live Demo & Support

* **Docs & live site**: [https://blindpeer.github.io/SpotifyNowPlayingScript-Local/](https://blindpeer.github.io/SpotifyNowPlayingScript-Local/)
* **Issues**: [https://github.com/blindpeer/SpotifyNowPlayingScript-Local/issues](https://github.com/blindpeer/SpotifyNowPlayingScript-Local/issues)

## Author & License

**Creator:** blind\_peer
**License:** PNC (see [LICENSE](LICENSE) for details)
