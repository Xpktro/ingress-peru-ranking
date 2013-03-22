#coding:utf8

from django.db import models
from common.datastructures import Enumeration

import strings


class PlayerManager(models.Manager):
    def ranking(self, lower=None, upper=None):
        return self.order_by('-ap', '-nickname')[lower:upper]


class Player(models.Model):

    FACTION_CHOICES = Enumeration([
        (0, 'RESISTANCE', strings.PLAYER_FACTION_RESISTANCE),
        (1, 'ENLIGHTENED', strings.PLAYER_FACTION_ENLIGHTENED),
    ])

    nickname = models.CharField(
        verbose_name=strings.PLAYER_NICKNAME,
        max_length=100,
        unique=True,
        null=False,
        blank=False
    )

    email = models.EmailField(
        verbose_name=strings.PLAYER_EMAIL,
        unique=True,
        null=False,
        blank=False
    )

    faction = models.PositiveIntegerField(
        verbose_name=strings.PLAYER_FACTION,
        choices=FACTION_CHOICES,
        null=False,
        blank=False
    )

    ap = models.PositiveIntegerField(
        verbose_name=strings.PLAYER_ACTION_POINTS,
        null=False,
        blank=False
    )

    level = models.PositiveIntegerField(
        verbose_name=strings.PLAYER_LEVEL,
        null=False,
        blank=False
    )

    objects = PlayerManager()

    def save(self, *args, **kwargs):
        self.level = self.calculate_level()
        super(Player, self).save(*args, **kwargs)

    def calculate_level(self):
        if self.ap < 10000:
            return 1
        elif self.ap < 30000:
            return 2
        elif self.ap < 70000:
            return 3
        elif self.ap < 150000:
            return 4
        elif self.ap < 300000:
            return 5
        elif self.ap < 600000:
            return 6
        elif self.ap < 1200000:
            return 7
        elif self.ap >= 1200000:
            return 8
        return 0

    def position(self):
        # Get the number of player above
        above = Player.objects.filter(ap__gt=self.ap).count()

        # Get the number of players with the same AP (if any) and use the
        # nickname as another ranking criteria.
        same = Player.objects.filter(ap=self.ap).order_by('-ap', '-nickname')

        # Then finally we return the position of the player in between their
        # neighbours and the number of players above.
        players_same_ap = [player.nickname for player in same]
        return above + players_same_ap.index(self.nickname) + 1

    def __unicode__(self):
        return self.nickname
