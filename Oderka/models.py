from django.db import models


class Club(models.Model):
    logoOfClub = models.ImageField(upload_to="Logo", null=True, blank=True)
    miniature = models.ImageField(upload_to="Miniatures", null=True, blank=True)
    nameOfClub = models.CharField(max_length=32, null=False, blank=False)
    description = models.TextField(max_length=516, null=True, blank=True)
    pictureOfClub = models.ImageField(upload_to="Picture Of Club", null=True, blank=True)

    def __str__(self):
        return self.nameOfClub


class ResultOfMatch(models.Model):
    matchResult = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.match_result()

    def match_result(self):
        return "{}".format(self.matchResult)


class TypeOfDetails(models.Model):
    type = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.details_type()

    def details_type(self):
        return "{}".format(self.type)


class Season(models.Model):
    season = models.CharField(max_length=32, null=False, blank=False)

    def __str__(self):
        return self.season


class Table(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    winsHome = models.PositiveSmallIntegerField(default=0, null=False, blank=False)
    drawsHome = models.PositiveSmallIntegerField(default=0, null=False, blank=False)
    losesHome = models.PositiveSmallIntegerField(default=0, null=False, blank=False)
    shotGoalsHome = models.PositiveSmallIntegerField(default=0, null=False, blank=False)
    lostGoalsHome = models.PositiveSmallIntegerField(default=0, null=False, blank=False)
    winsAway = models.PositiveSmallIntegerField(default=0, null=False, blank=False)
    drawsAway = models.PositiveSmallIntegerField(default=0, null=False, blank=False)
    losesAway = models.PositiveSmallIntegerField(default=0, null=False, blank=False)
    shotGoalsAway = models.PositiveSmallIntegerField(default=0, null=False, blank=False)
    lostGoalsAway = models.PositiveSmallIntegerField(default=0, null=False, blank=False)


    def __str__(self):
        return self.table()

    def table(self):
        return "{} {}".format(self.club, self.season)

    @property
    def wins(self):
        return self.winsHome + self.winsAway

    @property
    def loses(self):
        return self.losesHome + self.losesAway

    @property
    def draws(self):
        return self.drawsHome + self.drawsAway

    @property
    def shotGoals(self):
        return self.shotGoalsHome + self.shotGoalsAway

    @property
    def lostGoals(self):
        return self.lostGoalsHome + self.lostGoalsAway

    @property
    def points(self):
        return self.wins * 3 + self.draws

    @property
    def matches(self):
        return self.wins + self.draws + self.loses


class Match(models.Model):
    opponent = models.ForeignKey(Club, on_delete=models.CASCADE)
    odraGoal = models.PositiveSmallIntegerField(default=0, null=False, blank=False)
    opponentGoal = models.PositiveSmallIntegerField(default=0, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    season = models.ManyToManyField(Season)
    result = models.ForeignKey(ResultOfMatch, on_delete=models.CASCADE)
    comment = models.TextField(max_length=516, null=False, blank=False)

    def __str__(self):
        return self.match_result()

    def match_result(self):
        return "({}) -- LZS Odra Słup {} : {} {}".format(self.date, self.odraGoal, self.opponentGoal, self.opponent)


class Player(models.Model):
    firstName = models.CharField(max_length=32, null=False, blank=False)
    secondName = models.CharField(max_length=32, null=False, blank=False)
    birth = models.DateField(null=True, blank=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="players_picture", null=True, blank=True)
    numberOfPlayer = models.PositiveSmallIntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.player_details()

    def player_details(self):
        return "{} {}".format(self.firstName, self.secondName)


class Details(models.Model):
    type = models.ForeignKey(TypeOfDetails, on_delete=models.CASCADE)
    who = models.ForeignKey(Player, on_delete=models.CASCADE)
    minute = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    match = models.ManyToManyField(Match)

    def __str__(self):
        return self.match_details()

    def match_details(self):
        return "{} - {} ({} Minuta)".format(self.type, self.who, self.minute)


class PicturesOfMatch(models.Model):
    pictures = models.ImageField(upload_to="pictures_of_match", null=True, blank=True)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    def __str__(self):
        return self.picture_of_match()

    def picture_of_match(self):
        return "{}".format(self.pictures)
