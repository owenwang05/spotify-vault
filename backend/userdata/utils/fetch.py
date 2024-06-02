import requests, typing
from userdata.models import Profile, Snapshot
from userdata.serializers import SnapshotSerializer

def get_profile(access_token: str) -> dict:
    # TODO this function will get data for a userpage from the Spotify API 
    # and return a dictionary with the same fields as the Snapshot model
    #
    # In addition to returning immediate information, it should cache that 
    # data as a snapshot by either:
    # 1. overwriting the last stored snapshot if Profile.cached == True
    # or 2. create a new snapshot with the data and setting Profile.cached to True
    raise TypeError("need to implement get_profile")

def save_profile(access_token: str) ->  bool:
    # TODO this function will save the last cached profile data to the 
    # database and return True if successful, False if not.
    #
    # If there is no cached data for a profile, then do not change anything
    # and return False
    #
    # Otherwise, set Profile.cached to False to mark the last snapshot as saved
    raise TypeError("need to implement __save_profile")
