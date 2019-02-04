from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class RouteManager(models.Manager):
    def create_route(self, user ,name):
        route = self.create(user=user, name=name)
        return route


class EventManager(models.Manager):
    def create_event(self, route, latitude, longitude, hour, date):
        event = self.create(route=route, latitude=latitude,
                            longitude=longitude, hour=hour, date=date)
        return event


class Route(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)

    objects = RouteManager()

class GeoEvent(models.Model):
    route = models.ForeignKey(Route, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    hour = models.TimeField()
    date = models.DateField()

    objects = EventManager()
