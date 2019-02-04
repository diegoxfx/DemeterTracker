from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.gis.geoip2 import GeoIP2
from rest_framework.authtoken.models import Token
from ipware import get_client_ip
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
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def start_tracking(request):
    #route = models.Route()
    #request.session['route'] = route
    ip, is_routable = get_client_ip(request)
    print(ip)
    #g = GeoIP()
    request.session['is_tracking'] = True
    #return render(request, 'location.html')
    return redirect('confirm')

def stop_tracking(request):
    request.session['is_tracking'] = False
    return redirect('confirm')


def confirm(request):
    ip, is_routable = get_client_ip(request)
    token, _ = Token.objects.get_or_create(user=request.user)
    return render(request, 'home.html', {'is_tracking': request.session['is_tracking'], 'ip': token})

def create_route(request):
    form = forms.RouteFormSet()
    return render(request, 'routes/new_route.html', {'formset': form})


def list_routes(request):
    form = forms.RouteList
    return render(request, 'routes/draw_route.html', {'form': form})


def list_events(request):
    table = tables.EventTable(models.Event.objects.filter(user=request.user))

    return render(request, 'tables/event_list.html', {
        'table': table
        })
