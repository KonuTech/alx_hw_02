# iot_control/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_device, name='register_device'),
    path('send/<str:device_id>/', views.send_message, name='send_message'),
    path('status/<str:device_id>/', views.device_status, name='device_status'),
    path('device_status/', views.device_status, name='device_status'),
    # Other URL patterns for iot_control app...
]
