from django.forms import ModelForm, inlineformset_factory
from models import models
from django.contrib.auth.models import User

EventFormSet = inlineformset_factory(User, models.Event,
                                     fields=('latitude', 'longitude', 'hour', 'date'),
                                     extra=1, can_delete=False, max_num=1)
