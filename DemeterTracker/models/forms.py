from django.forms import ModelForm, inlineformset_factory, Form, ModelChoiceField
from models import models
from django.contrib.auth.models import User

RouteFormSet = inlineformset_factory(User, models.Route,
                                     fields=('name',),
                                     extra=1, can_delete=False, max_num=1,
                                     validate_max=True)

class ModelChoiceRoute(ModelChoiceField):
    def label_from_instance(self, obj):
                return obj.name

class RouteList(Form):
    routes = ModelChoiceRoute(queryset = models.Route.objects.all(), initial=0)
