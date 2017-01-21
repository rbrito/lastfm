#!/bin/env/python3

import json
import urllib.parse
import urllib.request

BASE_URL = 'http://ws.audioscrobbler.com/2.0/?'

# api_key kindly stolen from: https://github.com/ubitux/DynaMPD/
BASE_PARAMS = {
    'api_key': 'b25b959554ed76058ac220b7b2e0a026',
    'format': 'json',
}


def get_similar_artists_url(artist, limit=5):
    used_params = {
        'method': 'artist.getSimilar',
        'artist': artist,
        'limit': limit,
    }

    # To avoid using Python 3.5's syntax of {**used_params, **BASE_PARAMS}
    used_params.update(BASE_PARAMS)
    query_string = urllib.parse.urlencode(used_params)

    return BASE_URL + query_string


def get_similar_tracks_url(artist, track, limit=5):
    used_params = {
        'method': 'track.getSimilar',
        'artist': artist,
        'track': track,
        'limit': limit,
    }

    # To avoid using Python 3.5's syntax of {**used_params, **BASE_PARAMS}
    used_params.update(BASE_PARAMS)
    query_string = urllib.parse.urlencode(used_params)

    return BASE_URL + query_string


def get_json(url):
    with urllib.request.urlopen(url) as f:
        data_str = f.read().decode()

    data = json.loads(data_str)
    return data


def list_top_similar_artists(query_artist):
    url = get_similar_artists_url(query_artist)
    artists = get_json(url)['similarartists']['artist']

    for artist in artists:
        print('Artist: %s, Similarity: %.2f%%' % (artist['name'],
                                                  100 * float(artist['match'])))
