# iot_control/models.py

from django.db import models

class Device(models.Model):
    device_id = models.CharField(max_length=20)
    device_type = models.CharField(max_length=50)
    # Add other fields as needed

    def __str__(self):
        return self.device_id
