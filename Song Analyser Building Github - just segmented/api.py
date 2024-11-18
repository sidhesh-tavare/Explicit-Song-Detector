# api.py

import requests
import lyricsgenius
from config import apikey

genius = lyricsgenius.Genius(apikey)

def fetch_song_details(song_id):
    """Fetch details of a specific song using its ID."""
    base_url = "https://api.genius.com"
    song_url = f"{base_url}/songs/{song_id}"
    headers = {'Authorization': f'Bearer {apikey}'}
    
    response = requests.get(song_url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error fetching song details: {response.status_code} - {response.text}")
        return None

    return response.json()['response']['song']

def search_song(query):
    """Search for a song based on the user input."""
    results = genius.search(query)
    return results
