from django.db import models
from django.conf import settings

from django.db import models
from django.db.models import Q

User = settings.AUTH_USER_MODEL

class PlayerQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    def search(self,query,user=None):
        lookup = Q(fullName__icontains=query) | Q(nationalTeamName__icontains = query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = self.filter(user = user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs
class PlayerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return PlayerQuerySet(self.model, using=self._db)
    def search(self, query, user=None):
        return self.get_queryset().search(query,user)

class Player(models.Model):
    objects = PlayerManager()
    public = models.BooleanField(default=True)
    user = models.ForeignKey(User, default= 1, null=True,on_delete=models.SET_NULL)
    acceleration = models.IntegerField()
    age = models.IntegerField(null=True)
    aggression = models.IntegerField()
    agility = models.IntegerField()
    attackingWorkRate = models.CharField(max_length=10)
    balance = models.IntegerField()
    ballcontrol = models.IntegerField()
    basestats = models.IntegerField()
    bestPosition = models.CharField(max_length=10)
    camRating = models.IntegerField()
    cbRating = models.IntegerField()
    cdmRating = models.IntegerField()
    cfRating = models.IntegerField()
    clubJerseyNumber = models.CharField(max_length=10)
    clubName = models.CharField(max_length=50)
    clubPosition = models.CharField(max_length=10)
    cmRating = models.IntegerField()
    color = models.CharField(max_length=20)
    composure = models.IntegerField()
    contractUntil = models.CharField(max_length=10)
    crossing = models.IntegerField()
    curve = models.IntegerField()
    defendingTotal = models.IntegerField()
    defensiveWorkRate = models.CharField(max_length=10)
    dribbling = models.IntegerField()
    dribblingTotal = models.IntegerField()
    finishing = models.IntegerField()
    freekickAccuracy = models.IntegerField()
    fullName = models.CharField(max_length=100)
    gkRating = models.IntegerField()
    goalkeeperDiving = models.IntegerField()
    goalkeeperHandling = models.IntegerField()
    goalkeeperPositioning = models.IntegerField()
    goalkeeperReflexes = models.IntegerField()
    goalkeeperkicking = models.IntegerField()
    headingAccuracy = models.IntegerField()
    height_inCm = models.IntegerField()
    id = models.AutoField(primary_key=True)
    imageLink = models.URLField(max_length=200)
    interceptions = models.IntegerField()
    internationalReputation = models.IntegerField()
    joinedOn = models.IntegerField()
    jumping = models.IntegerField()
    knownAs = models.CharField(max_length=50)
    lbRating = models.IntegerField()
    lfRating = models.IntegerField()
    lmRating = models.IntegerField()
    longShots = models.IntegerField()
    longpassing = models.IntegerField()
    lwRating = models.IntegerField()
    lwbRating = models.IntegerField()
    marking = models.IntegerField()
    nationalTeamImageLink = models.URLField(max_length=200)
    nationalTeamJerseyNumber = models.CharField(max_length=10)
    nationalTeamName = models.CharField(max_length=50)
    nationalTeamPosition = models.CharField(max_length=10)
    nationality = models.CharField(max_length=50)
    onLoan = models.CharField(max_length=10)
    overall = models.IntegerField()
    paceTotal = models.IntegerField()
    passingTotal = models.IntegerField()
    penalties = models.IntegerField()
    physicalityTotal = models.IntegerField()
    positioning = models.IntegerField()
    positionsPlayed = models.CharField(max_length=10)
    potential = models.IntegerField()
    preferredFoot = models.CharField(max_length=10)
    rbRating = models.IntegerField()
    reactions = models.IntegerField()
    releaseClause = models.BigIntegerField()
    rfRating = models.IntegerField()
    rmRating = models.IntegerField()
    rwRating = models.IntegerField()
    rwbRating = models.IntegerField()
    shootingTotal = models.IntegerField()
    shortPassing = models.IntegerField()
    shotPower = models.IntegerField()
    skillMoves = models.IntegerField()
    slidingTackle = models.IntegerField()
    sprintSpeed = models.IntegerField()
    stRating = models.IntegerField()
    stamina = models.IntegerField()
    standingTackle = models.IntegerField()
    strength = models.IntegerField()
    totalstats = models.IntegerField()
    value_inEuro = models.BigIntegerField()
    vision = models.IntegerField()
    volleys = models.IntegerField()
    wage_inEuro = models.IntegerField()
    weakFootRating = models.IntegerField()
    weight_inKg = models.IntegerField()

    def get_id(self):
        return self.id
    def get_valueByWage(self):
        return "%.2f"% (self.overall/(self.wage_inEuro/10000))
    def __str__(self):
        return self.fullName