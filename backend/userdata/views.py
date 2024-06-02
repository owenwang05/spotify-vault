from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from userdata.models import Profile, Snapshot
from userdata.serializers import SnapshotSerializer

from .utils import fetch

# Create your views here.
@csrf_exempt
def profile(request, access_token):
    if request.method == 'GET': # get most recent profile data
        try:
            data = fetch.get_profile(access_token) # TODO get_profile
            response = SnapshotSerializer(data)
            return JsonResponse(response.data)
        except:
            print("Unable to get profile")

    if request.method == "POST": # save profile
        try:
            success = fetch.save_profile(access_token) # TODO save_profile 
            if not success: return HttpResponse(status=425)
        except:
            return HttpResponse(status=500)
                
    return HttpResponse(status=404)

def snapshot(request, access_token, snapshot_index):
    # Return profile data for a profile snapshot given the index
    return JsonResponse({})

def snapshot_list(request, access_token):
    # Return a list of all snapshots for a given profile and their dates
    return JsonResponse({})