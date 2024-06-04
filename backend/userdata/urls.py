from django.urls import path
from userdata import views

urlpatterns = [
    path('create/<slug:access_token>/', views.create_profile),
    path('recent/<slug:access_token>/', views.get_profile),
    path('save/<slug:access_token>/', views.save_snapshot),
    path('snapshots/<slug:access_token>/', views.list_snapshots),
    path('snapshots/<slug:access_token>/<int:snapshot_index>', views.get_snapshot)
]