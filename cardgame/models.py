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
