from django.db import models


class Club(models.Model):
    pictureOfClub = models.ImageField(upload_to="Logo", null=True, blank=True)
    nameOfClub = models.CharField(max_length=32, null=False, blank=False)
    description = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nameOfClub


class ResultOfMatch(models.Model):
    matchResult = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.match_result()

    def match_result(self):
        return "{}".format(self.matchResult)


class Match(models.Model):
    opponent = models.ForeignKey(Club, on_delete=models.CASCADE)
    odraGoal = models.PositiveSmallIntegerField(default=0, null=False, blank=False)
    opponentGoal = models.PositiveSmallIntegerField(default=0, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    result = models.ForeignKey(ResultOfMatch, on_delete=models.CASCADE)

    def __str__(self):
        return self.match_result()

    def match_result(self):
        return "Odra Słup {} : {} {} - {}".format(self.odraGoal, self.opponentGoal, self.opponent, self.date)


class Player(models.Model):
    firstName = models.CharField(max_length=32, null=False, blank=False)
    secondName = models.CharField(max_length=32, null=False, blank=False)
    birth = models.DateField(null=True, blank=False)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="players_picture", null=True, blank=True)
