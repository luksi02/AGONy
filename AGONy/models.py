from random import randint, choice

from django.db import models
from django.contrib.auth.models import User

RACE = [
    (0, "Human"),
    (1, "Elf"),
    (2, "Dwarf"),
]

CREATURE_TYPE = [
    (0, "Human"),
    (1, "Wildlife"),
    (2, "Undead"),
]

class HeroRace(models.Model):
    race = models.IntegerField(choices=RACE, default=0)


class Hero(models.Model):
    RACE = [
        (0, "Human"),
        (1, "Elf"),
        (2, "Dwarf"),
        ]
    name = models.CharField(max_length=50, unique=True)
    #race = models.IntegerField(default=0) #choices=RACE, default=0)
    hp = models.IntegerField(default=100)
    attack = models.IntegerField(default=5)
    defence = models.IntegerField(default=5)
    backstory = models.TextField(blank=True, default='')
    #weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, null=True)
    #armor = models.ForeignKey(Armor, on_delete=models.CASCADE, null=True)
    #owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name}"




class MonsterType(models.Model):
    monster_type = models.IntegerField(choices=CREATURE_TYPE, default=0)


class Monster(models.Model):
    name = models.CharField(max_length=50)
    hp = models.IntegerField(default=100)
    attack = models.IntegerField()
    defence = models.IntegerField()
    #monster_level=models.IntegerField()
    #monster_type = (Undead/Wildlife/Human)
    #description

    def __str__(self):
        return f"{self.name}"





# Create your models here.
