from django.urls import path
from userdata import views

urlpatterns = [
    path('create/', views.create_profile),
    path('recent/', views.get_profile),
    path('save/', views.save_snapshot),
    path('delete/', views.delete_profile),
    path('snapshots/', views.list_snapshots),
    path('snapshots/<int:snapshot_index>/', views.get_snapshot)
]