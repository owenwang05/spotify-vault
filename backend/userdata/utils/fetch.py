import requests, typing
from userdata.models import Profile, Snapshot
from userdata.serializers import SnapshotSerializer

def get_profile(access_token: str) -> dict:
    # TODO Need to 
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
        for i in user_snapshots:
            print(i.top_genres)

    except: 
        # create new profile in database 
        user_profile = Profile.objects.create(snapshot_cached=False, user_id=json_response["id"])
        print(user_profile.user_id)
        user_profile.save()

def __update_snapshot():
    # TODO helper function to overwrite cached snapshot
    return 

def save_profile(access_token: str) ->  bool:
    # TODO this function will save the last cached profile data to the 
    # database and return True if successful, False if not.
    #
    # If there is no cached data for a profile, then do not change anything
    # and return False
    #
    # Otherwise, set Profile.cached to False to mark the last snapshot as saved
    raise TypeError("need to implement __save_profile")

def retrieve_snapshot(access_token: str, snapshot_index: int) -> dict: 
    """
    Retrieves a snapshot for a given profile given the index 

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
        user_id = response["id"]
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
        user_id = response["id"]
        snapshots = Profile.objects.get(user_id=user_id).snapshot_set.order_by('-snapshot_date')
        snapshot_dates = [i[0] for i in snapshots.values_list('snapshot_date')]
    except:
        return []
    
    return snapshot_dates