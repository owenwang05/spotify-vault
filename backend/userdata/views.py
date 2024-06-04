from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from userdata.models import Profile, Snapshot
from userdata.serializers import SnapshotSerializer

from .utils import fetch

# TODO views are temporarily csrf_exempt  only for testing

@csrf_exempt
def create_profile(request, access_token):
    if request.method == 'GET':
        status = fetch.create_profile(access_token)
        if status:
            return JsonResponse({'status': 201}, status=201)
    return JsonResponse({'status': 404}, status=404)

@csrf_exempt
def get_profile(request, access_token):
    if request.method == 'GET':
        try:
            data = fetch.get_profile(access_token) # TODO get_profile
            response = SnapshotSerializer(data)
            return JsonResponse(response.data)
        except:
            print("Unable to get profile")
    return JsonResponse({'status': 404}, status=404)

@csrf_exempt
def save_snapshot(request, access_token):
    # Save the most recent data access to the database
    if request.method == 'GET':
        try:
            success = fetch.save_snapshot(access_token) # TODO save_profile 
            if not success: return JsonResponse({'status': 425}, status=425)
        except:
            print("Unable to save profile")
    return JsonResponse({'status': 404}, status=404)

def list_snapshots(request, access_token):
    # Returns a list of all snapshot dates for a profile
    if request.method == 'GET':
        data = fetch.list_snapshot_dates(access_token)
        if(data):
            return JsonResponse(dict(enumerate(data)))
    return JsonResponse({'status': 404}, status=404)

def get_snapshot(request, access_token, snapshot_index):
    # Return data for a profile snapshot given the index
    if request.method == 'GET':
        data = fetch.get_snapshot(access_token, snapshot_index)
        if(data):
            return JsonResponse(data)
    return JsonResponse({'status': 404}, status=404)