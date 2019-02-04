import django_tables2 as tables
from models import models

class RouteTable(tables.Table):
    class Meta:
        model = models.Route

