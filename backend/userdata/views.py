from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

from userdata.models import Profile, Snapshot
from userdata.serializers import SnapshotSerializer

from .utils import fetch

@csrf_exempt
def create_profile(request):
    # Create a profile in the database
    if request.method == 'POST':
        access_token = request.headers['Authorization']
        response = fetch.create_profile(access_token)
        return JsonResponse(**response._asdict())
    return HttpResponse(status=404)

@csrf_exempt
def get_profile(request):
    # Retrieve most recent profile data
    if request.method == 'GET':
        access_token = request.headers['Authorization']            
        response = fetch.get_profile(access_token)
        return JsonResponse(**response._asdict())
    return HttpResponse(status=404)

# this is csrf protected as it's the only destructive action.
def delete_profile(request):
    # Delete profile from database
    if request.method == 'DELETE':
        access_token = request.headers['Authorization']
        response = fetch.delete_profile(access_token)
        return JsonResponse(**response._asdict())
    return HttpResponse(status=404)

@csrf_exempt
def save_snapshot(request):
    # Save the most recent data access to the database
    if request.method == 'POST':
        access_token = request.headers['Authorization']
        response = fetch.save_snapshot(access_token)
        return JsonResponse(**response._asdict())
    return HttpResponse(status=404)

@csrf_exempt
def list_snapshots(request):
    # Returns a list of all snapshot dates for a profile
    if request.method == 'GET':
        access_token = request.headers['Authorization']
        response = fetch.list_snapshot_dates(access_token)
        return JsonResponse(**response._asdict())
    return JsonResponse(data="Invalid request", status=400)

@csrf_exempt
def get_snapshot(request, snapshot_index):
    # Return data for a profile snapshot given the index
    if request.method == 'GET':
        access_token = request.headers['Authorization']
        response = fetch.get_snapshot(access_token, snapshot_index)
        return JsonResponse(**response._asdict())
    return JsonResponse(data="Invalid request", status=400)