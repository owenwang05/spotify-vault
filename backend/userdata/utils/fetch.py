from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from userdata.models import Profile, TOP_GENRES_LENGTH, TOP_LIST_LENGTH
from userdata.serializers import SnapshotSerializer

import requests, typing
from collections import namedtuple
import time
from datetime import datetime, timezone as dt_tz

Response = namedtuple('Response', ['status', 'data'])

def create_profile(access_token: str) -> Response:
    """
    Creates a profile and an empty cached snapshot. If profile exists, do nothing.

    Args: 
        Pass in one but not the other:
        user_id (str): 
        access_token (str): the Spotify API access token for retrieving user id

    Returns: 
        A Response namedtuple where data will have a message on whether the process
        was successful or not.
    """
    # fetch user_id from Spotify API
    if not access_token: return Response(status=400, data={'message': 'Invalid access token'})

    response = requests.get("https://api.spotify.com/v1/me", headers={
        "Authorization": f"Bearer {access_token}"
    }).json()

    # if the profile already exists, then don't bother creating the profile
    try:
        user_id = response['id']
    except KeyError:
        return Response(status=400, data={'message': "Invalid access token"})
    
    if Profile.objects.filter(user_id=user_id).exists():
        return Response(status=200, data={'message': "Profile already exists"})

    # otherwise create and save a new profile with a cached snapshot
    Profile.objects.create(user_id=user_id, snapshot_cached=False)
    # passes in data already retrieved into __update_cache
    profile_data = {
        'user_id': user_id,
        'username': response['display_name'],
        'avatar_url': response['images'][1]['url'] if len(response['images']) > 0 else ""
    }
    # __update_cache creates a new cached snapshot and saves it to the database
    status = __update_cache(access_token, profile_data=profile_data)
    if status:
        return Response(status=201, data={'message': "Profile created"})
    else:
        return Response(status=500, data={'message': "No valid cached snapshot"})


def get_profile(access_token: str) -> Response:
    """
    Gets most recent profile data and last save date. Handles backend snapshot caching

    Args: 
        access_token (str): the Spotify API access token for retrieving user id

    Returns: 
        A Response namedtuple where data will be a dictionary with the data if
        the request succeeds.
    """
    # in case of invalid access token, return error
    if not access_token: return Response(status=400, data={'message': "Invalid access token"})

    # fetch user profile data from Spotify API
    response = requests.get("https://api.spotify.com/v1/me", headers={
        "Authorization": f"Bearer {access_token}"
    }).json()
    
    try:
        user_id = response['id']
    except KeyError:
        return Response(status=400, data={'message': "Invalid access token"})
    
    try:
        # fetch existing profile 
        profile = Profile.objects.get(user_id=user_id)
    except ObjectDoesNotExist:
        return Response(status=400, data={'message': "Profile needs to be created"})

    # fetch all user snapshots
    profile_data = {
        'user_id': response['id'],
        'username': response['display_name'],
        'avatar_url': response['images'][1]['url'] if len(response['images']) > 0 else ""
    }   
    
    if __update_cache(access_token, profile_data):
        current_snapshot = profile.snapshot_set.order_by('-date')[0]
        serializer = SnapshotSerializer(current_snapshot)
        return Response(status=200, data=serializer.data)
    else:
        return Response(status=404, data={'message': "No valid cached snapshot"}) 


def __update_cache(access_token: str, profile_data: dict={}) -> bool: # TODO 
    """
    Updates a snapshot cache for a profile to have the most recent data. If there
    is no cache in the database, this function will create one.

    Args: 
        access_token (str): the Spotify API access token for retrieving user id

    Returns: 
        True if the cache was updated successfully, False otherwise.
    """
    # in case of invalid access token, return error
    if not access_token: return False

    # create a dictionary to hold all Snapshot field assignments
    assign = {
        'username': 'null',
        'avatar_url': '',
        'listening_time': 0,
        'top_genres': [],
        'top_songs': [],
        'top_artists': [],
    }

    # retrieve data for profile information either from API or from parameter
    if not profile_data:
        response = requests.get("https://api.spotify.com/v1/me", headers={
        "Authorization": f"Bearer {access_token}"
        }).json()

        try:
            user_id = response['id']
        except:
            print("Invalid access token")
            return False
        assign['username'] = response['display_name']
        assign['avatar_url'] = response['images'][1]['url'] if len(response['images']) > 0 else ""
    else:
        try:
            user_id = profile_data['user_id']
        except KeyError:
            print("Unable to fetch user_id from parameter")
            return False
        # get intersecting key-pairs between parameter dictionary and assign dictionary
        profile_data = {key: profile_data[key] for key in assign.keys() & profile_data.keys()}
        # union the two dictionaries where parameters will take precedent
        assign = assign | profile_data
        
    # Calculate listening time in the last 24 hours
    fetch_time = int(time.time_ns() / 1000000) - 86400000
    listening_time = 0
    # iterate through recently played songs until all songs in last 24 hours are retrieved and processed
    response = requests.get(f"https://api.spotify.com/v1/me/player/recently-played?limit=50&after={fetch_time}", headers={
        "Authorization": f"Bearer {access_token}"
    }).json()
    # loop through each song in the recently played response and add to listening_time
    if 'items' in response:
        for item in response['items']:
            listening_time += item['track']['duration_ms']
    assign['listening_time'] = listening_time

    # Get top songs in last 4 weeks 
    top_songs = {
        'songs': []
    }
    response = requests.get(f"https://api.spotify.com/v1/me/top/tracks?offset=0&limit={TOP_LIST_LENGTH}&time_range=short_term", headers={
        "Authorization": f"Bearer {access_token}"
    }).json()

    if 'items' in response:
        for item in response['items']:
            top_songs['songs'].append({'name': item['name'], 'image': item['album']['images'][0], 'artist': item['artists'][0]['name']})
    
    assign['top_songs'] = top_songs

    # Get top artists and process top genres in last 4 weeks
    top_artists = {
        'artists': []
    }
    genre_log = {}
    response = requests.get(f"https://api.spotify.com/v1/me/top/artists?offset=0&limit=50&time_range=short_term", headers={
        "Authorization": f"Bearer {access_token}"
    }).json()
    if 'items' in response:
        for item in response['items']:
            if len(top_artists['artists']) < TOP_LIST_LENGTH:
                top_artists['artists'].append({'name': item["name"], 'image': item['images'][0]})

            for genre in item['genres']:
                if genre in genre_log:
                    genre_log[genre] += 1
                else:
                    genre_log[genre] = 1
    genre_log = sorted(genre_log.items(), key=lambda item: item[1], reverse=True)
    top_genres = [item[0] for item in genre_log[:TOP_GENRES_LENGTH]]
    assign['top_genres'] = top_genres
    assign['top_artists'] = top_artists

    # store data in database
    try:
        profile = Profile.objects.get(user_id=user_id)
        # if a Snapshot is cached, retrieve the most recent snapshot
        if profile.snapshot_cached: 
            snapshot = profile.snapshot_set.order_by('-date')[0]
        # Otherwise create a new one
        else:
            snapshot = profile.snapshot_set.create()
            profile.snapshot_cached = True
        
        # Assign new values into cached snapshot
        for (key, value) in assign.items():
            setattr(snapshot, key, value)

        snapshot.save()
        profile.save()
        return True
    
    except ObjectDoesNotExist:
        print("Unable to fetch snapshot")
        return False


def save_snapshot(access_token: str) -> Response:
    """
    Saves currently cached snapshot for a profile into the database permanently if
    no snapshot was recently saved.

    Args: 
        access_token (str): the Spotify API access token for retrieving user id

    Returns: 
        A Response namedtuple which may include a message on whether the process
        was successful or not.
    """
    # in case of invalid access token, return error
    if not access_token: return Response(status=400, data={'message': "Invalid access token"})

    # fetch user profile data from Spotify API
    response = requests.get("https://api.spotify.com/v1/me", headers={
        "Authorization": f"Bearer {access_token}"
    }).json()

    try:
        user_id = response['id']
    except KeyError:
        return Response(status=400, data={'message': "Invalid access token"})
    
    # Retrieve profile from database and check for cached
    try:
        profile = Profile.objects.get(user_id=user_id)
        if profile.recently_saved():
            return Response(status=403, data={'message': "Last snapshot saved too recently"})

        if profile.snapshot_cached:
            profile.snapshot_cached = False
            profile.last_saved = timezone.now()
            profile.save()
            return Response(status=200, data={'message': "Snapshot saved"})
        else:
            return Response(status=404, data={'message': "No valid cached snapshot"})
    except ObjectDoesNotExist:
        return Response(status=404, data={'message': "Profile needs to be created"})


def get_snapshot(access_token: str, snapshot_index: int) -> Response: 
    """
    Retrieves a snapshot for a profile given the index of the snapshot

    Args: 
        access_token (str): the Spotify API access token for retrieving user id
        snapshot_index (int): index of the snapshot to delete where 0 is the most recent
    Returns: 
        A Response namedtuple where data will have a dictionary with the data.
    """
    # in case of invalid access token, return error
    if not access_token: return Response(status=400, data={'message': "Invalid access token"})

    # Fetch user profile data from Spotify API
    response = requests.get("https://api.spotify.com/v1/me", headers={
        "Authorization": f"Bearer {access_token}"
    }).json()

    # Retrieves snapshot from the database 
    try:
        user_id = response['id']
    except KeyError:
        return Response(status=400, data={'message': "Invalid access token"})
    
    try:
        profile = Profile.objects.get(user_id=user_id)
    except ObjectDoesNotExist:
        return Response(status=404, data={'message': "Profile needs to be created"})
    
    try:
        snapshot = profile.snapshot_set.order_by('-date')[snapshot_index]
        return Response(status=200, data=SnapshotSerializer(snapshot).data)
    except IndexError:
        return Response(status=404, data={'message': "Invalid snapshot index"})


def list_snapshot_dates(access_token: str) -> Response:
    """
    Returns a list of all snapshot's save dates for a given profile

    Args: 
        access_token (str): the Spotify API access token for retrieving user id
        snapshot_index (int): index of the snapshot to delete where 0 is the most recent

    Returns: 
        A Response namedtuple where data will have an indexed dictionary of snapshot dates.
    """

    # in case of invalid access token, return error
    if not access_token: return Response(status=400, data={'message': "Invalid access token"})

    # Fetch user profile data from Spotify API
    response = requests.get("https://api.spotify.com/v1/me", headers={
        "Authorization": f"Bearer {access_token}"
    }).json()

    # Fetch the list of snapshot dates from the database
    try:
        user_id = response['id']
    except KeyError:
        return Response(status=400, data={'message': "Invalid access token"})
    
    try:
        profile = Profile.objects.get(user_id=user_id)
    except ObjectDoesNotExist:
        return Response(status=404, data={'message': "Profile needs to be created"})
    
    snapshots = profile.snapshot_set.order_by('-date')
    snapshot_data = snapshots.values('date', 'listening_time') # get only the date and listening time for each snapshot
    snapshot_data = dict(enumerate(snapshot_data))
    snapshot_data['length'] = len(snapshot_data)

    return Response(status=200, data=snapshot_data)


def delete_profile(access_token: str) -> Response:
    """
    Deletes a profile and its snapshots from the database

    Args: 
        access_token (str): the Spotify API access token for retrieving user id

    Returns: 
        A Response namedtuple where data may include a message on whether the process was successful.
    """
    # in case of invalid access token, return error
    if not access_token: return Response(status=400, data={'message': "Invalid access token"})

    # fetch user profile data from Spotify API
    response = requests.get("https://api.spotify.com/v1/me", headers={
        "Authorization": f"Bearer {access_token}"
    }).json()
    
    try:
        user_id = response['id']
    except KeyError:
        return Response(status=400, data={'message': "Invalid access token"})
    
    try:
        profile = Profile.objects.get(user_id=user_id)
        profile.delete()
        return Response(status=200, data={'message': "Profile was deleted"})
    except ObjectDoesNotExist:
        return Response(status=404, data={'message': "Profile needs to be created"})