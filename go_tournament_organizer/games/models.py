from django.db import models

# Create your models here.

class Game(models.Model):
    opponent_white = models.CharField(max_length=255)
    opponent_black = models.CharField(max_length=255)
    result = models.CharField(max_length=255, default=None, blank=True, null=True)
    handicap = models.CharField(max_length=255, default=None, blank=True, null=True)

    def __str__(self):
        output = self.opponent_white + " with white against " + self.opponent_black + " with black."
        if self.handicap:
            output += " Handicap: " + self.handicap
        if self.result:
            output += " Result: " + self.result
        output += "\n"
        return output
