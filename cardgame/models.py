from django.db import models
from django.db.models import CASCADE


class Player(models.Model):
    name = models.CharField('Player name', max_length=50)
    wins_count = models.PositiveIntegerField('Number of wins', default=0)

    def __str__(self):
        return self.name


class Statistic(models.Model):
    game_date = models.DateTimeField(auto_now_add=True)
    winner = models.ForeignKey('Player', verbose_name='Winner', on_delete=CASCADE)


class GameData(models.Model):
    deck = models.CharField(max_length=80, default=[])
    board = models.CharField(max_length=250, default=[])
    card = models.CharField(max_length=3, default='')
    game_participants = models.CharField(max_length=250, default=[])
    who_turn = models.PositiveIntegerField(default=0)
    game_status = models.BooleanField(default=False)
    is_draw = models.BooleanField(default=False)
    turn_count = models.PositiveIntegerField(default=0)
