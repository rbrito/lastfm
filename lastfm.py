#!/bin/env/python3

import json
import urllib.request

url = 'http://ws.audioscrobbler.com/2.0/?api_key=b25b959554ed76058ac220b7b2e0a026&format=json'

def get_similar_artists_url(artist, limit=5):
    return url + '&method=artist.getSimilar' + '&artist=' + artist + '&limit=' + str(limit)

def get_similar_tracks_url(artist, track, limit=5):
    return url + '&method=track.getSimilar' + '&artist=' + artist + '&track=' + track + '&limit=' + str(limit)

def get_json(url):
    with urllib.request.urlopen(url) as f:
        data_str = f.read().decode()

    data = json.loads(data_str)
    return data


def list_top_similar_artists(query_artist):
    artists = get_json(get_similar_artists_url(query_artist))['similarartists']['artist']

    for artist in artists:
        print('Artist: %s, Similarity: %.2f%%' %(artist['name'], 100 * float(artist['match'])))
