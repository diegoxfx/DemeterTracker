from django.forms import ModelForm, inlineformset_factory
from models.models import Event
from django.contrib.auth.models import User

EventFormSet = inlineformset_factory(User, Event,
                                     fields=('latitude', 'longitude', 'hour', 'date'),
                                     extra=1, can_delete=False)
