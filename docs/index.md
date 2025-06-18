# SpotifyNowPlayingScript-Local
Spotify Now Playing Script (Local) is a small, self-hosted tool that lets you post your current Spotify “Now Playing” into any chat client via a simple `/me` command.  It uses a browser bookmarklet plus two lightweight local servers (an HTTP redirect page and a Flask proxy) to handle Spotify’s PKCE OAuth flow, token exchange, and silent refresh.
