from django.urls import path
from userdata import views

urlpatterns = [
    path('<slug:access_token>/', views.profile),
    path('<slug:access_token>/list', views.snapshot_list),
    path('<slug:access_token>/<int:snapshot_index>', views.snapshot)
]