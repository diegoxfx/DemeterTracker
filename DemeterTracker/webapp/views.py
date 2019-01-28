from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
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


def new_event(request):
    if request.method == 'POST':
        form = forms.EventFormSet(request.POST, instance=request.user)
        if form.is_valid():
            event = form.save()
            return redirect('home')
    else:
        form = forms.EventFormSet()
        return render(request, 'registration/new_event.html', {'formset': form})     


def list_events(request):
    table = tables.EventTable(models.Event.objects.filter(user=request.user))

    return render(request, 'tables/event_list.html', {
        'table': table
        })
