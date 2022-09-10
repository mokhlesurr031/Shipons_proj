from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('traffic/', views.traffic_data),
    path('by_license/<str:license>/', views.all_data_by_license_plate),
    path('traffic_timestamp/', views.traffic_timestamp),
    path('traffic_timestamp/cam_id/<str:cam_id>/', views.traffic_timestamp_by_cam),
    path('traffic_timestamp/cam_id/<str:cam_id>/<int:entry_id>/', views.traffic_timestamp_by_cam_id_id)
]