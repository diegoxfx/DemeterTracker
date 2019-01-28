import django_tables2 as tables
from models import models

class EventTable(tables.Table):
    class Meta:
        model = models.Event

