from django.db import models


class Bus(models.Model):
    driver_id = models.IntegerField(primary_key=True)
    driver_name = models.CharField(max_length=200)
    bus_no = models.IntegerField()

class Attendent(models.Model):
    att_id = models.IntegerField(primary_key=True)
    att_name = models.CharField(max_length=200)
    bus = models.ForeignKey(Bus)

class BusTrip(models.Model):
    trip_type = models.IntegerField()
    start_time = models.DateTimeField('start time')
    end_date = models.DateTimeField('end time')
    bus = models.ForeignKey(Bus)

