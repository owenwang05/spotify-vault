from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from userdata.models import Profile
from userdata.serializers import SnapshotSerializer

import requests, typing


def create_profile(access_token: str) -> bool:
    """
    Creates a profile and an empty cached snapshot

    Args: 
        access_token (str): the spotify api access token passed from the front end

    Returns: 
        True if profile was created successfully, False if not
    """
    if not access_token: return False

    url = "https://api.spotify.com/v1/me/"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }  
    response = requests.get(url, headers=headers)
    json_response = response.json()

    # if the profile already exists, then don't bother creating the profile
    if Profile.objects.filter(user_id=json_response["id"]).exists():
        return False

    # otherwise create and save a new profile with a cached snapshot
    user_profile = Profile.objects.create(user_id=json_response["id"], snapshot_cached=False)
    # passes in data already retrieved into __update_cache
    try:
        profile_data = {
            'user_id': json_response["id"],
            'username': json_response["display_name"],
            'profile_picture': json_response["images"][1]["url"] if len(json_response["images"]) > 0 else ""
        }
    except KeyError:
        return False
    
    # __update_cache creates a new cached snapshot and saves it to the database
    status = __update_cache(access_token, profile_data=profile_data)
    return status


def get_profile(access_token: str) -> dict: # TODO
    """
    Gets most recent profile data and handles backend snapshot caching

    Args: 
        access_token (str): the spotify api access token passed from the front end

    Returns: 
        a dictionary with the data to be displayed on the page, or an empty dictionary
        in the case of an error.
    """
    # in case of invalid access token, return error
    if not access_token: return {}

    # fetch data user profile data from Spotify API
    url = "https://api.spotify.com/v1/me/"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }  
    response = requests.get(url, headers=headers)
    json_response = response.json()
    
    try:
        # fetch existing profile 
        user_profile = Profile.objects.get(user_id=json_response["id"])
        
        # fetch all user snapshots
        user_snapshots = user_profile.snapshot_set.all()

        # update snapshot and turn it into a dictionary using snapshot serializer 
        # TODO

    except ObjectDoesNotExist: 
        return {}


def __update_cache(access_token: str, profile_data: dict={}) -> bool: # TODO 
    """
    Updates a snapshot cache for a profile to have the most recent data. If there
    is no cache in the database, this function will create one.

    Args: 
        access_token (str): the spotify api access token passed from the front end

    Returns: 
        a dictionary with the data to be displayed on the page, or an empty dictionary
        in the case of an error.
    """

    if not access_token: return False

    # create a dictionary to hold all Snapshot field assignments
    assign = {
        'username': 'null',
        'avatar_url': '',
        'listening_time': 0,
        'top_genres': [],
        'song_ids': [],
        'artist_ids': [],
    }

    # retrieve data for profile information either from API or from parameter
    if not profile_data:
        url = "https://api.spotify.com/v1/me/"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }  
        response = requests.get(url, headers=headers)
        json_response = response.json()

        user_id = json_response['id']
        assign['username'] = json_response['display_name']
        assign['profile_picture'] = json_response['images'][1]["url"] if len(json_response["images"]) > 0 else ""
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
        
    ###################################################################
    # TODO retrieve data for listening time, top songs, artists, etc. #
    ###################################################################

    # if a Snapshot is cached, retrieve the most recent snapshot
    try:
        profile = Profile.objects.get(user_id=user_id)

        if profile.snapshot_cached:
            snapshot = profile.snapshot_set.order_by('-snapshot_date')[0]
        else:
            snapshot = profile.snapshot_set.create()
            profile.snapshot_cached = True

        for (key, value) in assign.items():
            setattr(snapshot, key, value)

        profile.save()
        return True
    
    except ObjectDoesNotExist:
        print("Unable to fetch snapshot")
        return False


def save_snapshot(access_token: str, profile_data: dict={}) ->  bool:
    # TODO this function will save the last cached profile data to the 
    # database and return True if successful, False if not.
    #
    # If there is no cached data for a profile, then do not change anything
    # and return False
    #
    # Otherwise, set Profile.cached to False to mark the last snapshot as saved
    raise TypeError("need to implement save_snapshot")


def retrieve_snapshot(access_token: str, snapshot_index: int) -> dict: 
    """
    Retrieves a snapshot for a profile given the index of the snapshot

    Args: 
        access_token (str): the spotify api access token for retrieving user id
        snapshot_index (int): the index of the snapshot where 0 is the most recent,
                              and subsequent numbers are later.

    Returns: 
        a dictionary with the data from the snapshot, or an empty dictionary in the 
        case of an error.
    """
    # in case of invalid access token, return error
    if not access_token: return {}

    # Fetch user profile data from Spotify API
    response = requests.get("https://api.spotify.com/v1/me", headers={
        "Authorization": f"Bearer {access_token}"
    }).json()

    # Retrieves snapshot from the database 
    try:
        user_id = response['id']
        profile = Profile.objects.get(user_id=user_id)
        snapshot = profile.snapshot_set.order_by('-snapshot_date')[snapshot_index]
    except:
        return {}

    # Serializes the model into a python dictionary and returns it
    return SnapshotSerializer(snapshot).data

def list_snapshot_dates(access_token: str) -> list:
    """
    Returns a list of all snapshot's save dates for a given profile

    Args: 
        access_token (str): the spotify api access token for retrieving user id
        snapshot_index (int): the index of the snapshot where 0 is the most recent,
                              and subsequent numbers are later.

    Returns: 
        a dictionary with the data from the snapshot, or an empty dictionary in the 
        case of an error.
    """

    # in case of invalid access token, return error
    if not access_token: return []

    # Fetch user profile data from Spotify API
    response = requests.get("https://api.spotify.com/v1/me", headers={
        "Authorization": f"Bearer {access_token}"
    }).json()

    # Fetch the list of snapshot dates from the database
    try:
        user_id = response['id']
        snapshots = Profile.objects.get(user_id=user_id).snapshot_set.order_by('-snapshot_date')
        snapshot_dates = [i[0] for i in snapshots.values_list('snapshot_date')]
    except:
        return []
    
    return snapshot_dates