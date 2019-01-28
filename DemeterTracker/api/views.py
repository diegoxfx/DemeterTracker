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
    user = request.user
    latitude = request.data.get("latitude")
    longitude = request.data.get("longitude")
    hour = request.data.get("hour")
    date = request.data.get("date")

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

    event = models.Event.objects.create_event(user, latitude, longitude, hour, date)
    event.save()
    return Response('event created successfully', status=HTTP_200_OK)
