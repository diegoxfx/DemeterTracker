from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class EventManager(models.Manager):
    def create_event(self, user, latitude, longitude, hour, date):
        event = self.create(user=user, latitude=latitude, longitude=longitude, hour=hour, date=date)
        return event

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    hour = models.TimeField()
    date = models.DateField()

    objects = EventManager()


class Route(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    hour = models.TimeField()
    date = models.DateField()

    objects = EventManager()
