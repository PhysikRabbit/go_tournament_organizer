from django.db import models

# Create your models here.


class RuleSet(models.Model):
    rule_set = models.CharField(max_length=500)
    allowed_board_sizes = models.PositiveSmallIntegerField()
    time_model = models.CharField(max_length=1000)
    komi = models.FloatField()
    handicap = models.CharField(max_length=1000)


class Participants(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    strength = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    club = models.CharField(max_length=100)
    dob = models.DateTimeField('Date of Birth')
    age = models.SmallIntegerField()


class Games(models.Model):
    tournament = models.ForeignKey('Tournament', related_name="game_tournament", on_delete=models.CASCADE)
    board_size = models.PositiveSmallIntegerField()
    white_player = models.ForeignKey(Participants, related_name="white_player", on_delete=models.CASCADE)
    black_player = models.ForeignKey(Participants, related_name="black_player", on_delete=models.CASCADE)
    result = models.CharField(max_length=100)


class Tournament(models.Model):
    name = models.CharField(max_length=500)
    rule_set = models.ForeignKey(RuleSet, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    notes = models.TextField()
    players = models.ForeignKey(Participants, on_delete=models.CASCADE)
    games = models.ForeignKey(Games, related_name="tournament_game", on_delete=models.CASCADE)
    result = models.FileField()
