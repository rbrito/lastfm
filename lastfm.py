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


def create_url_string(params):
    """
    Internal function to create an URL-encoded version of the parameters
    passed in as an argument merged with those in the BASE_PARAMS
    dictionary.
    """
    updated_params = {**params, **BASE_PARAMS}
    query_string = urllib.parse.urlencode(updated_params)

    return BASE_URL + query_string


def get_similar_artists_url(artist, limit=5):
    used_params = {
        'method': 'artist.getSimilar',
        'artist': artist,
        'limit': limit,
    }

    return create_url_string(used_params)


def get_similar_tracks_url(artist, track, limit=5):
    used_params = {
        'method': 'track.getSimilar',
        'artist': artist,
        'track': track,
        'limit': limit,
    }

    return create_url_string(used_params)


def get_json(url):
    """
    Given a URL, make a network request, transform the JSON response into a
    Python dictionary and return that dictionary.
    """
    with urllib.request.urlopen(url) as f:
        data_str = f.read().decode()

    data = json.loads(data_str)
    return data


def list_top_similar_artists(query_artist):
    url = get_similar_artists_url(query_artist)
    artists = get_json(url)['similarartists']['artist']

    for artist in artists:
        print('Artist: %s, Similarity: %.2f%%' %
              (artist['name'], 100 * float(artist['match'])))


def list_top_similar_tracks(query_artist, query_track):
    url = get_similar_tracks_url(query_artist, query_track)
    tracks = get_json(url)['similartracks']['track']

    for track in tracks:
        print('Track: %s, Artist: %s, Similarity: %.2f%%' %
              (track['name'], track['artist']['name'], 100 * float(track['match'])))
