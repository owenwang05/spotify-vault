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

    if access_token:
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

    else:
        # return an error for frontend to use 
        return {}

def __update_snapshot():
    pass

def save_profile(access_token: str) ->  bool:
    # TODO this function will save the last cached profile data to the 
    # database and return True if successful, False if not.
    #
    # If there is no cached data for a profile, then do not change anything
    # and return False
    #
    # Otherwise, set Profile.cached to False to mark the last snapshot as saved
    raise TypeError("need to implement __save_profile")
