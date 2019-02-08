from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token
from django.forms import Form
from models import models
from models import forms
from models import tables

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def create_route(request):
    form = forms.RouteFormSet()
    return render(request, 'routes/new_route.html', {'formset': form})


def list_routes(request):
    class RouteList(Form):
        routes = forms.ModelChoiceRoute(queryset =
            models.Route.objects.filter(user=request.user).all(), initial=0)
    route_form = RouteList
    return render(request, 'routes/draw_route.html', {'form': route_form})


def list_events(request):
    table = tables.EventTable(models.Event.objects.filter(user=request.user))

    return render(request, 'tables/event_list.html', {
        'table': table
        })
