from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from models import models

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def new_event(request):
    route_id = request.data.get("route_id")
    latitude = request.data.get("latitude")
    longitude = request.data.get("longitude")
    hour = request.data.get("hour")
    date = request.data.get("date")

    if route_id is None:
        return Response({'error': 'Please provide route id'},
                        status=HTTP_400_BAD_REQUEST)

    if latitude is None:
        return Response({'error': 'Please provide latitude'},
                       status=HTTP_400_BAD_REQUEST)

    if longitude is None:
        return Response({'error': 'Please provide longitude'},
                       status=HTTP_400_BAD_REQUEST)

    if hour is None:
        return Response({'error': 'Please provide hour'},
                       status=HTTP_400_BAD_REQUEST)

    if date is None:
        return Response({'error': 'Please provide date'},
                       status=HTTP_400_BAD_REQUEST)

    route = models.Route.objects.get(id=route_id)

    event = models.GeoEvent.objects.create_event(route, latitude, longitude,
                                              hour, date)
    event.save()
    return Response('event created successfully', status=HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])
def new_route(request):
    user = request.user
    name = request.data.get("name")

    if name is None:
        return Response({'error': 'Please provide a name'},
                        status=HTTP_400_BAD_REQUEST)

    route = models.Route.objects.create_route(user, name)
    route.save()
    return Response({'id': route.id}, status=HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])
def route_events(request):
    route_id = request.data.get("id")
    route = models.Route.objects.get(id=route_id)

    if route_id is None:
        return Response({'error': 'Please provide an id'},
                        status=HTTP_400_BAD_REQUEST)

    events = models.GeoEvent.objects.filter(route=route).all()
    events_coords = []

    for event in events:
        coords = {'lat': event.latitude, 'lng': event.longitude}
        events_coords.append(coords)
    return Response(events_coords, status=HTTP_200_OK)
