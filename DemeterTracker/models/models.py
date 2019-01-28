from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    def create_event(self, user, latitude, longitude, hour, date):
        event = self.create(user=user, latitude=latitude, hour=hour, date=date)
        return event
    
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    hour = models.TimeField()
    date = models.DateField()
