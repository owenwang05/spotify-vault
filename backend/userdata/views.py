from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from userdata.models import Profile, Snapshot
from userdata.serializers import SnapshotSerializer

from .utils import fetch
import requests

# Create your views here.
@csrf_exempt
def profile(request, access_token):
    data = fetch.get_profile(access_token)
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
    if request.method == "GET":
        data = fetch.get_snapshot(access_token, snapshot_index)
        if(data):
            return JsonResponse(data)
        return HttpResponse(status=404)

def snapshot_list(request, access_token):
    # Return a list of all snapshots for a given profile and their dates
    if request.method == "GET":
        data = fetch.list_snapshot_dates(access_token)
        if(data):
            return JsonResponse(dict(enumerate(data)))
        return HttpResponse(status=404)