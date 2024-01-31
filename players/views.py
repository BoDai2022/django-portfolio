from django.http import Http404
from rest_framework import authentication,generics,mixins,permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Player
from .serializers import PlayerSerializer
from api.permissions import IsManagerPlayerEditorPermission
from api.authentication import TokenAuthentication
from api.mixins import ManagerPlayerEditorPermissionMixin, UserQuerySetMixin

class PlayerDetailAPIView(UserQuerySetMixin,ManagerPlayerEditorPermissionMixin,generics.RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
# class PlayerUpdateAPIView(generics.UpdateAPIView):
#     queryset = Player.objects.all()
#     serializer_class = PlayerSerializer
class PlayerUpdateAPIView(ManagerPlayerEditorPermissionMixin,generics.UpdateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    lookup_field = 'pk'

    def perform_update(self,serializer):
        age = serializer.validated_data.get("age") or None
        if not age:
            age = 18
        instance = serializer.save(age=age) 
class PlayerDeleteAPIView(ManagerPlayerEditorPermissionMixin,generics.DestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    lookup_field = 'pk'    
# class PlayerCreateAPIView(generics.CreateAPIView):
#     queryset = Player.objects.all()
#     serializer_class = PlayerSerializer
#     def perform_create(self, serializer):
#         age = serializer.validated_data.get("age") or None
#         if not age:
#             age = 18
#         serializer.save(age=age)
class PlayerListCreateAPIView(UserQuerySetMixin,ManagerPlayerEditorPermissionMixin,generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    # authentication_classes = [authentication.SessionAuthentication,
    #                         #   authentication.TokenAuthentication]
    #                          TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.DjangoModelPermissions]
    # permission_classes = [permissions.IsAdminUser,IsManagerPlayerEditorPermission]
    def perform_create(self, serializer):
        age = serializer.validated_data.get("age") or None
        if not age:
            age = 18
        serializer.save(user=self.request.user,age=age)  
    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     print(request.user)
    #     return qs.filter(user = request.user)      
# class PlayerListAPIView(generics.ListAPIView):
#     queryset = Player.objects.all()
#     serializer_class = PlayerSerializer


class PlayerMixinView(ManagerPlayerEditorPermissionMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    lookup_field = 'pk'
    def get(self,request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)
    def post(self, request, *args,**kwargs):
        return self.create(request, args, kwargs)
    ## put and delete
# function based view
@api_view(['GET','POST'])
def player_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            obj = get_object_or_404(Player, pk=pk)
            data = PlayerSerializer(obj,many=False).data
            return Response(data)        
        queryset = Player.objects.all()
        data = PlayerSerializer(queryset,many=True).data
        return Response(data)

    if method == "POST":
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            age = serializer.validated_data.get("age") or None
            if not age:
                age = 18
            serializer.save(age=age)               
            return Response(serializer.data)
        return Response({"invalid": "not good data"},status=400)