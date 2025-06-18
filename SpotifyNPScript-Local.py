#!/usr/bin/env python3
"""
Spotify NP Script (Local Edition) v1.4
Maker: blind_peer

Scaffold script that:
  1. Prompts for your Spotify Client ID.
  2. Generates the core files:
     - index.html
     - proxy.py
     - run-proxy-py.bat
     - run-all-servers.bat
  3. Creates a Python virtualenv (`venv`) and installs Flask + dependencies.
  4. Writes `bookmarklet.txt` containing the one-line bookmarklet.
  5. Offers to start the local servers immediately.
"""

import os
import sys
import subprocess
from textwrap import dedent

# Raw string so backslashes aren’t escapes; includes a literal '{cid}' placeholder
BOOKMARKLET = r"""javascript:(async()=>{const CLIENT_ID='{cid}',REDIR='http://127.0.0.1:8000/index.html';function genR(n){const A='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789',U=new Uint8Array(n);crypto.getRandomValues(U);return[...U].map(i=>A[i%A.length]).join('')}async function sha256(s){return crypto.subtle.digest('SHA-256',new TextEncoder().encode(s))}function b64u(b){return btoa(String.fromCharCode(...new Uint8Array(b))).replace(/=/g,'').replace(/\+/g,'-').replace(/\//g,'_')}async function postNow(){let t=localStorage.getItem('sp_access_token'),r=await fetch('https://api.spotify.com/v1/me/player/currently-playing',{headers:{Authorization:'Bearer '+t}});if(r.status===401){localStorage.removeItem('sp_access_token');return initAuth()}if(r.status===204)return;if(!r.ok)return;const d=await r.json(),i=d.item,a=i.artists.map(x=>x.name).join(', '),nm=i.name,al=i.album.name,url=i.external_urls.spotify;cb().say(`/me is now playing: ${a} - ${nm} [${al}] (${url})`)}async function initAuth(){const v=genR(64),c=b64u(await sha256(v)),s=b64u(new TextEncoder().encode(v)),p=new URLSearchParams({response_type:'code',client_id:CLIENT_ID,scope:'user-read-currently-playing',redirect_uri:REDIR,code_challenge_method:'S256',code_challenge:c,state:s});const w=window.open('https://accounts.spotify.com/authorize?'+p,'SpotifyAuth','width=450,height=730');if(!w)alert('Please allow pop-ups to authenticate with Spotify.')}window.addEventListener('message',e=>{if(e.data.access_token){localStorage.setItem('sp_access_token',e.data.access_token);localStorage.setItem('sp_refresh_token',e.data.refresh_token);postNow()}});localStorage.getItem('sp_access_token')?postNow():initAuth();})();"""

def write_file(path, content):
    """Write the given content (dedented) to the specified file."""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(dedent(content).lstrip())

def main():
    # 1) Prompt for Spotify Client ID
    cid = input("Enter your Spotify Client ID: ").strip()
    if not cid:
        print("Error: Client ID is required.")
        sys.exit(1)

    print("\n[✔] Generating files in:", os.getcwd(), "\n")

    # 2) index.html
    write_file("index.html", f"""
    <!DOCTYPE html>
    <html>
    <head><meta charset="utf-8"><title>Spotify Auth Redirect</title></head>
    <body>
    <script>
    (async () => {{
      const params = new URLSearchParams(window.location.search);
      const code   = params.get('code');
      const state  = params.get('state');
      if (!code || !state) {{
        document.body.textContent = '⚠️ Missing code or state in URL.';
        return;
      }}
      function fromBase64Url(str) {{
        str = str.replace(/-/g,'+').replace(/_/g,'/');
        while (str.length % 4) str += '=';
        return atob(str);
      }}
      const codeVerifier   = fromBase64Url(state);
      const TOKEN_ENDPOINT = 'http://127.0.0.1:8888/api/token';
      try {{
        const resp = await fetch(TOKEN_ENDPOINT, {{
          method: 'POST',
          headers: {{ 'Content-Type':'application/x-www-form-urlencoded' }},
          body: new URLSearchParams({{
            grant_type:      'authorization_code',
            code:            code,
            redirect_uri:    location.origin + location.pathname,
            client_id:       '{cid}',
            code_verifier:   codeVerifier
          }})
        }});
        const data = await resp.json();
        if (!resp.ok) throw new Error(`${{data.error}}: ${{data.error_description}}`);
        if (window.opener) {{
          window.opener.postMessage({{
            access_token:  data.access_token,
            refresh_token: data.refresh_token
          }}, '*');
        }}
        document.body.textContent = '✅ Tokens saved! You can close this window.';
        window.close();
      }} catch (err) {{
        document.body.innerHTML =
          '⚠️ Error exchanging token:<br><pre style="color:red;">' + err + '</pre>';
        console.error('Token exchange failed:', err);
      }}
    }})();
    </script>
    </body>
    </html>
    """)
    print("[✔] index.html")

    # 3) proxy.py
    write_file("proxy.py", f"""
    #!/usr/bin/env python3
    # proxy.py for Spotify NP Script (Local Edition) v1.4

    from flask import Flask, request, jsonify
    from flask_cors import CORS
    import requests

    CLIENT_ID = '{cid}'
    app = Flask(__name__)
    CORS(app, origins='http://127.0.0.1:8000')
    SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'

    @app.route('/api/token', methods=['POST'])
    def exchange_code():
        payload = request.form.to_dict()
        r = requests.post(SPOTIFY_TOKEN_URL, data=payload,
                          headers={{'Content-Type':'application/x-www-form-urlencoded'}})
        return jsonify(r.json()), r.status_code

    @app.route('/api/refresh', methods=['POST'])
    def refresh_token():
        payload = {{
            'grant_type': 'refresh_token',
            'refresh_token': request.form.get('refresh_token'),
            'client_id': CLIENT_ID
        }}
        r = requests.post(SPOTIFY_TOKEN_URL, data=payload,
                          headers={{'Content-Type':'application/x-www-form-urlencoded'}})
        return jsonify(r.json()), r.status_code

    if __name__ == '__main__':
        app.run(host='127.0.0.1', port=8888)
    """)
    print("[✔] proxy.py")

    # 4) run-proxy-py.bat
    write_file("run-proxy-py.bat", """
    @echo off
    cd /d "%~dp0"
    if not exist venv\\Scripts\\activate.bat (
      py -3 -m venv venv
    )
    call venv\\Scripts\\activate.bat
    pip install flask requests flask-cors >nul
    python proxy.py
    pause
    """)
    print("[✔] run-proxy-py.bat")

    # 5) run-all-servers.bat
    write_file("run-all-servers.bat", """
    @echo off
    cd /d "%~dp0"
    start "RedirectServer" /min py -3 -m http.server 8000
    start "SpotifyProxy"  /min "%~dp0run-proxy-py.bat"
    exit
    """)
    print("[✔] run-all-servers.bat")

    # 6) bookmarklet.txt
    bm = BOOKMARKLET.replace("{cid}", cid)
    with open("bookmarklet.txt", "w", encoding="utf-8") as f:
        f.write(bm)
    print("[✔] bookmarklet.txt")

    # 7) Set up venv & install dependencies
    if not os.path.isdir("venv"):
        print("\n[+] Creating Python virtualenv…")
        subprocess.check_call([sys.executable, "-m", "venv", "venv"])
    print("[+] Installing Python dependencies…")
    activate = os.path.join("venv", "Scripts", "activate.bat")
    subprocess.call(f'call "{activate}" && pip install flask requests flask-cors >nul', shell=True)

    # 8) Prompt to start servers
    ans = input("\nStart both servers now? (Y/N): ").strip().lower()
    if ans == 'y':
        print("Launching servers…")
        subprocess.Popen(["run-all-servers.bat"], shell=True)
    else:
        print("You can start them later with run-all-servers.bat")

    print("\nDone! Enjoy Spotify NP Script (Local Edition) v1.4")
    input("Press Enter to exit…")

if __name__ == "__main__":
    main()
