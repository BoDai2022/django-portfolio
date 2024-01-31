from rest_framework import mixins,viewsets

from .models import Player
from .serializers import PlayerSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    """
    get -> list -> QuerySet
    get -> retrieve -> Product Instance Detail View
    post -> create -> New Instance
    put -> Update
    patch -> Partial Update
    delete -> destroy
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    lookup_field = 'pk'

class PlayerGernericViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    get -> list -> QuerySet
    get -> retrieve -> Product Instance Detail View
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    lookup_field = 'pk'

# player_list_view = PlayerGernericViewSet.as_view({"get":"list"})
# player_detail_view = PlayerGernericViewSet.as_view({"get":"retrieve"})