from rest_framework import serializers
from rest_framework.reverse import reverse_lazy as reverse
from .models import Player
# from .validators import validate_fullName
from api.serializers import UserPublicSerializer

class PlayerSerializer(serializers.ModelSerializer):
    my_user_data = serializers.SerializerMethodField(read_only = True)
    owner = UserPublicSerializer(source= "user", read_only = True)
    # owner = serializers.CharField(source="user.username", read_only=True)
    valueByWage = serializers.SerializerMethodField(read_only = True)
    url = serializers.SerializerMethodField(read_only = True)
    alt_url = serializers.HyperlinkedIdentityField(view_name="player-detail",lookup_field='pk')
    # id = serializers.SerializerMethodField(read_only = True)
    # fullName = serializers.CharField(validators = [validate_fullName])
    # email = serializers.EmailField(write_only = True)
    id = serializers.IntegerField(source = 'pk', read_only = True)
    # xxx = serializers.IntegerField(source = 'user.xxx', read_only = True)
    class Meta:
        model = Player
        fields = [
            'owner',
            'my_user_data',
            'url',
            'alt_url',
            'id',
            'pk',
            'acceleration',
            'age',
            'aggression',
            'agility',
            'attackingWorkRate',
            'balance',
            'ballcontrol',
            'basestats',
            'bestPosition',
            'camRating',
            'cbRating',
            'cdmRating',
            'cfRating',
            'clubJerseyNumber',
            'clubName',
            'clubPosition',
            'cmRating',
            'color',
            'composure',
            'contractUntil',
            'crossing',
            'curve',
            'defendingTotal',
            'defensiveWorkRate',
            'dribbling',
            'dribblingTotal',
            'finishing',
            'freekickAccuracy',
            'fullName',
            'gkRating',
            'goalkeeperDiving',
            'goalkeeperHandling',
            'goalkeeperPositioning',
            'goalkeeperReflexes',
            'goalkeeperkicking',
            'headingAccuracy',
            'height_inCm',
            'interceptions',
            # 'id',
            "imageLink",
            'internationalReputation',
            'joinedOn',
            'jumping',
            'knownAs',
            'lbRating',
            'lfRating',
            'lmRating',
            'longShots',
            'longpassing',
            'lwRating',
            'lwbRating',
            'marking',
            "nationalTeamImageLink",
            'nationalTeamJerseyNumber',
            'nationalTeamName',
            'nationalTeamPosition',
            'nationality',
            'onLoan',
            'overall',
            'paceTotal',
            'passingTotal',
            'penalties',
            'physicalityTotal',
            'positioning',
            'positionsPlayed',
            'potential',
            'preferredFoot',
            'rbRating',
            'reactions',
            'releaseClause',
            'rfRating',
            'rmRating',
            'rwRating',
            'rwbRating',
            'shootingTotal',
            'shortPassing',
            'shotPower',
            'skillMoves',
            'slidingTackle',
            'sprintSpeed',
            'stRating',
            'stamina',
            'standingTackle',
            'strength',
            'totalstats',
            'value_inEuro',
            'vision',
            'volleys',
            'wage_inEuro',
            'weakFootRating',
            'weight_inKg',
            'valueByWage'
        ]

    def get_valueByWage(self, obj):
        return obj.get_valueByWage()
    # def get_id(self, obj):
    #     return obj.get_id()
    def get_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("player-detail",kwargs = {"pk":obj.pk}, request= request)
    def get_my_user_data(self,obj):
        return {
            "username": obj.user.username
        }
    # def create(self, validated_data):
    #     #could send an email or do anything else here
    #     return super().create(validated_data)
    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)

    def validate_fullName(self,value):
        self.context.get("request")
        # qs = Player.objects.filter(fullName__exact = value)
        qs = Player.objects.filter(fullName__iexact = value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already existed")
        return value
    