from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from userdata.models import Profile, Snapshot
from userdata.serializers import SnapshotSerializer

from .utils import fetch

# TODO views are temporarily csrf_exempt  only for testing

@csrf_exempt
def create_profile(request, access_token):
    data = fetch.create_profile(access_token)
    return JsonResponse(**data._asdict())
    # Create a profile in the database
    if request.method == 'POST':
        response = fetch.create_profile(access_token)
        return JsonResponse(**response._asdict())
    return HttpResponse(status=404)

@csrf_exempt
def get_profile(request, access_token):
    data = fetch.get_profile(access_token)
    return JsonResponse(**data._asdict())
    # Retrieve most recent profile data
    if request.method == 'POST':
        response = fetch.get_profile(access_token)
        return JsonResponse(**response._asdict())
    return HttpResponse(status=404)

@csrf_exempt
def delete_profile(request, access_token):
    data = fetch.delete_profile(access_token)
    return JsonResponse(**data._asdict())
    # Delete profile from database
    if request.method == 'POST':
        response = fetch.delete_profile(access_token)
        return JsonResponse(**response._asdict())
    return HttpResponse(status=404)

@csrf_exempt
def save_snapshot(request, access_token):
    data = fetch.save_snapshot(access_token)
    return JsonResponse(**data._asdict())
    # Save the most recent data access to the database
    if request.method == 'POST':
        response = fetch.save_snapshot(access_token)
        return JsonResponse(**response._asdict())
    return HttpResponse(status=404)
    

def list_snapshots(request, access_token):
    # Returns a list of all snapshot dates for a profile
    if request.method == 'GET':
        response = fetch.list_snapshot_dates(access_token)
        return JsonResponse(**response._asdict())
    return HttpResponse(status=404)

def get_snapshot(request, access_token, snapshot_index):
    # Return data for a profile snapshot given the index
    if request.method == 'GET':
        response = fetch.get_snapshot(access_token, snapshot_index)
        return JsonResponse(**response._asdict())
    return HttpResponse(status=404)