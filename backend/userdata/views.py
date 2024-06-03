from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from userdata.models import Profile, Snapshot
from userdata.serializers import SnapshotSerializer

from .utils import fetch
import requests

# Create your views here.
@csrf_exempt
def profile(request, access_token):
    fetch.get_profile(access_token)
    # if request.method == 'GET': # get most recent profile data
    #     try:
    #         data = fetch.get_profile(access_token) # TODO get_profile
    #         response = SnapshotSerializer(data)
    #         return JsonResponse(response.data)
    #     except:
    #         print("Unable to get profile")

    # if request.method == "POST": # save profile
    #     try:
    #         success = fetch.save_profile(access_token) # TODO save_profile 
    #         if not success: return HttpResponse(status=425)
    #     except:
    #         return HttpResponse(status=500)
                
    return HttpResponse(status=404)

def snapshot(request, access_token, snapshot_index):
    # Return profile data for a profile snapshot given the index
    response = requests.get("https://api.spotify.com/v1/me", headers={
        "Authorization": f"Bearer {access_token}"
    }).json()

    try:
        user_id = response["id"]
    except:
        print("Failed to get profile")
        return HttpResponse(status=404)

    try:
        profile = Profile.objects.get(user_id=user_id)
    except:
        print("Profile has not been created in database")
        return HttpResponse(status=500)

    try:
        snapshot = profile.snapshot_set.order_by('-snapshot_date')[snapshot_index]
    except:
        print("Invalid snapshot index")
        return HttpResponse(status=500)

    return JsonResponse(SnapshotSerializer(snapshot).data)

def snapshot_list(request, access_token):
    # Return a list of all snapshots for a given profile and their dates

    return JsonResponse({})