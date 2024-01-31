from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Player

def validate_fullName(self,value):
    # qs = Player.objects.filter(fullName__exact = value)
    qs = Player.objects.filter(fullName__iexact = value)
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already existed")
    return value

# unique_full_name = UniqueValidator(queryset=Player.objects.all(), lookup="iexact")