from django.shortcuts import render
from rest_framework import generics
from players.models import Player
from players.serializers import PlayerSerializer
class SearchListView(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    results = Player.objects.none()
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        if q is not None:
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user=user)
        return results