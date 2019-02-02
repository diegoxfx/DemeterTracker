"""DemeterTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from webapp import views as webapp_views
from api import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('registration/', webapp_views.signup, name='signup'),
    path('events/start_tracking', webapp_views.start_tracking, name='start_tracking'),
    path('events/stop_tracking', webapp_views.stop_tracking, name='stop_tracking'),
    path('events/list_events', webapp_views.list_events, name='list_events'),
    path('confirm', webapp_views.confirm, name='confirm'),
    path('api/login', api_views.login),
    path('api/new_event', api_views.new_event)
]
