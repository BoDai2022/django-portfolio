from rest_framework import serializers

class UserPlayerInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="player-detail",
        lookup_field = "pk",
        read_only = True
    )
    name = serializers.CharField(source="fullName", read_only = True)

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only = True)
    id = serializers.IntegerField(read_only = True)
    other_players = serializers.SerializerMethodField(read_only = True)

    def get_other_players(self, obj):
        user = obj
        my_players_qs = user.player_set.all()[:2]
        return UserPlayerInlineSerializer(my_players_qs, many = True, context= self.context).data