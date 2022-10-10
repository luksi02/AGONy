from random import randint, choice

from django.db import models
from django.contrib.auth.models import User

"""
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
    
class MonsterType(models.Model):
    monster_type = models.IntegerField(choices=CREATURE_TYPE, default=0)
"""

class Hero(models.Model):

    RACE = [
        (0, "Human"),
        (1, "Elf"),
        (2, "Dwarf"),
        ]

    name = models.CharField(max_length=50, unique=True)
    race = models.IntegerField(choices=RACE, default=0)
    hp = models.IntegerField(default=100)
    attack = models.IntegerField(default=5)
    defence = models.IntegerField(default=5)
    backstory = models.TextField(blank=True, default='')
    gold = models.IntegerField(default=0)
    #weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, null=True)
    #armor = models.ForeignKey(Armor, on_delete=models.CASCADE, null=True)
    #owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name}"


class Monster(models.Model):

    CREATURE_TYPE = [
        (0, "Human"),
        (1, "Wildlife"),
        (2, "Undead"),
    ]

    CREATURE_LEVEL = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
    ]

    name = models.CharField(max_length=50)
    hp = models.IntegerField(default=20)
    attack = models.IntegerField(default=2)
    defence = models.IntegerField(default=2)
    monster_level = models.IntegerField(choices=CREATURE_LEVEL, default=0)
    monster_type = models.IntegerField(choices=CREATURE_TYPE, default=0)
    description = models.TextField(blank=True)
    monsters_gold = models.IntegerField(default=randint(5, 10))

    def __str__(self):
        return f"{self.name}"

"""class Journey(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    level = models.IntegerField()
    monsters = models.ManyToManyField('AliveMonster', through='AliveMonsterInStage')"""


class Event(models.Model):

    EVENT_TYPE = [
        (0, 'Monster Encounter'),
        (1, 'Loot Encounter'),
        (2, 'Trap Encounter')
    ]
    name = models.CharField(max_length=50)
    type = models.IntegerField(choices=EVENT_TYPE, default=0)


class Journal(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    event_description = models.TextField(blank=True)
    alive = models.BooleanField(default=True)


"""class Game(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    level = models.IntegerField()
    monsters = models.ManyToManyField('AliveMonster', through='AliveMonsterInStage')"""

class AliveMonster(models.Model):

    monster_class = models.ForeignKey(Monster, on_delete=models.CASCADE)
    current_hp = models.IntegerField(null=True)
    #current_attack = models.IntegerField(null=True)
    #current_defence = models.IntegerField(null=True)

    @property
    def attack(self):
        return self.monster_class.attack

    @property
    def defence(self):
        return self.monster_class.defence

    @property
    def name(self):
        return self.monster_class.name


class Stage(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE, default=0)
    level = models.IntegerField(default=0)
    monsters = models.ManyToManyField(AliveMonster, through='AliveMonsterInStage')
    visited = models.BooleanField(default=False)
    next_stage = models.ForeignKey("Stage", on_delete=models.SET_NULL, null=True, related_name='prev')

    def generate_monster(self):

        monster_list = Monster.objects.all()
        amount = randint(0, 3)
        for _ in range(amount):
            mc = choice(monster_list)
            extra_hp = randint(0,10)
            am = AliveMonster.objects.create(monster_class=mc, current_hp=mc.hp+extra_hp)
            AliveMonsterInStage.objects.create(stage=self, monster=am)

class AliveMonsterInStage(models.Model):

    monster = models.ForeignKey(AliveMonster, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    #journey = models.ForeignKey(Journey, on_delete=models.CASCADE)
