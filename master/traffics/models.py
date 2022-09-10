from django.db import models

# Create your models here.


class TrafficData(models.Model):
    license_plate = models.CharField(max_length=200)
    cam_id = models.CharField(max_length=200)
    count = models.IntegerField(default=1)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.license_plate


class TrafficTimeStamp(models.Model):
    traffic_id = models.ForeignKey(TrafficData, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        tid = str(self.traffic_id.id)
        return tid