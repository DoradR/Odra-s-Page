from django.db import models

class ResultOfMatch(models.Model):
    RESULT = {
        (0, 'Win'),
        (1, 'Tie'),
        (2, 'Lose')
    }

    matchResult = models.PositiveSmallIntegerField(default=0, choices=RESULT)

class Match(models.Model):
    opponent = models.CharField(max_length=64, null=False, blank=False)
    odraGoal = models.PositiveSmallIntegerField(default=0, null=False, blank=False)
    opponentGoal = models.PositiveSmallIntegerField(default=0, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    result = models.OneToOneField(ResultOfMatch, on_delete=models.CASCADE, null=False, blank=False)


    def __str__(self):
        return self.match_result()

    def match_result(self):
        return "Odra Słup {} : {} {}".format(self.odraGoal, self.opponent, self.opponentGoal)