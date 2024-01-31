from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from players.models import Player
from django.forms.models import model_to_dict
from players.serializers import PlayerSerializer
import json

# Create your views here.
@api_view(http_method_names=['POST'])
def api_home(request, *args, **kwargs):
    instance = Player.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(model_data,fields=['fullName','age'])
        data = PlayerSerializer(instance).data
    return Response(data)