#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Small Python 3.5+ module/program to query last.fm for similar artists or
tracks (which could be used to automatically add songs to currently running
music players, using songs that the user already has).

Copyright © 2017-2018 Rogério Theodoro de Brito.
"""

import json
import urllib.parse
import urllib.request

import argparse


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


def get_similar_artists_url(artist, limit=20):
    """
    Create an URL for getting similar artists from last.fm based on the
    input parameter artist.
    """
    used_params = {
        'method': 'artist.getSimilar',
        'artist': artist,
        'limit': limit,
    }

    return create_url_string(used_params)


def get_similar_tracks_url(artist, track, limit=20):
    """
    Create an URL for getting similar tracks from last.fm based on the
    input parameters artist and track.
    """
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
    with urllib.request.urlopen(url) as connection:
        data_str = connection.read().decode()

    data = json.loads(data_str)
    return data


def list_top_similar_artists(query_artist, quantity):
    """
    Print the top similar artists to query_artist.

    quantity: The number of similar artists to get from last.fm.
    """
    url = get_similar_artists_url(query_artist, quantity)
    artists = get_json(url)['similarartists']['artist']

    for artist in artists:
        print('Artist: %s, Similarity: %.2f%%' %
              (artist['name'], 100 * float(artist['match'])))


def list_top_similar_tracks(query_artist, query_track, quantity):
    """
    Print the top similar tracks to query_track by query_artist.

    quantity: The number of similar tracks to get from last.fm.
    """
    url = get_similar_tracks_url(query_artist, query_track, quantity)
    tracks = get_json(url)['similartracks']['track']

    for track in tracks:
        print('Track: %s, Artist: %s, Similarity: %.2f%%' %
              (track['name'], track['artist']['name'], 100 * float(track['match'])))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('artist')
    parser.add_argument('--track',
                        help='Track name to get similar tracks to.')
    parser.add_argument('--quantity',
                        help='Number of tracks or artists to get similar results to. (Default: 20)',
                        type=int,
                        default=20)

    args = parser.parse_args()

    if args.track:
        list_top_similar_tracks(args.artist, args.track, args.quantity)
    else:
        list_top_similar_artists(args.artist, args.quantity)
