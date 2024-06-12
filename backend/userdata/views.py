from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

from userdata.models import Profile, Snapshot
from userdata.serializers import SnapshotSerializer

from .utils import fetch

@csrf_exempt
def create_profile(request, access_token):
    # Create a profile in the database
    if request.method == 'POST':
        response = fetch.create_profile(access_token)
        return JsonResponse(**response._asdict())
    return HttpResponse(status=404)

@csrf_exempt
def get_profile(request, access_token):
    # Retrieve most recent profile data
    if request.method == 'POST':
        response = fetch.get_profile(access_token)
        return JsonResponse(**response._asdict())
    return HttpResponse(status=404)

@csrf_exempt
def delete_profile(request, access_token):
    # Delete profile from database
    if request.method == 'DELETE':
        response = fetch.delete_profile(access_token)
        return JsonResponse(**response._asdict())
    return HttpResponse(status=404)

@csrf_exempt
def save_snapshot(request, access_token):
    # Save the most recent data access to the database
    if request.method == 'POST':
        response = fetch.save_snapshot(access_token)
        return JsonResponse(**response._asdict())
    return HttpResponse(status=404)

@ensure_csrf_cookie
def list_snapshots(request, access_token):
    # Returns a list of all snapshot dates for a profile
    if request.method == 'GET':
        response = fetch.list_snapshot_dates(access_token)
        return JsonResponse(**response._asdict())
    return JsonResponse(data="Invalid request", status=400)

@ensure_csrf_cookie
def get_snapshot(request, access_token, snapshot_index):
    # Return data for a profile snapshot given the index
    if request.method == 'GET':
        response = fetch.get_snapshot(access_token, snapshot_index)
        return JsonResponse(**response._asdict())
    return JsonResponse(data="Invalid request", status=400)