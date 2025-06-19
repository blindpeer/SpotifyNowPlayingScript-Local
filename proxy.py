#!/usr/bin/env python3
# proxy.py for Spotify NP Script (Local Edition) v1.5

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

CLIENT_ID = 'YOUR_SPOTIFY_CLIENT_ID'
app = Flask(__name__)
CORS(app, origins='http://127.0.0.1:8000')
SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'

@app.route('/api/token', methods=['POST'])
def exchange_code():
    payload = request.form.to_dict()
    r = requests.post(SPOTIFY_TOKEN_URL, data=payload,
                      headers={'Content-Type':'application/x-www-form-urlencoded'})
    return jsonify(r.json()), r.status_code

@app.route('/api/refresh', methods=['POST'])
def refresh_token():
    payload = {
        'grant_type': 'refresh_token',
        'refresh_token': request.form.get('refresh_token'),
        'client_id': CLIENT_ID
    }
    r = requests.post(SPOTIFY_TOKEN_URL, data=payload,
                      headers={'Content-Type':'application/x-www-form-urlencoded'})
    return jsonify(r.json()), r.status_code

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888)

