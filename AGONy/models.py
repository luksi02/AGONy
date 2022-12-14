from random import randint, choice
from PIL import Image

from django.db import models
from django.contrib.auth.models import User


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
    defence = models.IntegerField(default=0)
    backstory = models.TextField(blank=True, default='')
    gold = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, null=True)
    # armor = models.ForeignKey(Armor, on_delete=models.CASCADE, null=True)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name}"


class MonsterImage(models.Model):
    monster_image = models.ImageField(upload_to='monster_images/uploaded', null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class MonsterAIDescription(models.Model):
    monster_AI_description = models.TextField(max_length=500, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)

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
    
    #monster_image = models.ForeignKey(MonsterImage, on_delete=models.CASCADE, blank=True, null=True)
    # for now I use ManyToMany field

    monster_monster_image = models.ManyToManyField(MonsterImage, through='MonsterMonsterImage', blank=True, null=True)

    monster_AI_description = models.ForeignKey(MonsterAIDescription, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class MonsterMonsterImage(models.Model):
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE)
    monster_image = models.ForeignKey(MonsterImage, on_delete=models.CASCADE)


class Origin(models.Model):
    ORIGIN_TYPE = [
        (0, 'General'),
        (1, 'TragicOrigin'),
        (2, 'Racial')
    ]

    origin_type = models.IntegerField(choices=ORIGIN_TYPE, default=0)
    origin_description = models.TextField(blank=True)


class EventImage(models.Model):
    event_image = models.ImageField(upload_to='event_images/uploaded', null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class EventAIDescription(models.Model):
    event_AI_description = models.TextField(max_length=500, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Event(models.Model):
    EVENT_TYPE = [
        (0, 'Monster Encounter'),
        (1, 'Loot Encounter'), # gold/items
        (2, 'Trap Encounter'), #damage
        (3, 'Empty Encounter'),  # beautiful views and so on.
        (4, 'Ambush - fight'), #fight with creature with no option of running away
        (5, 'Visitable place'), #visitable place - crypt/monster lair with high possiblity of hi-level creature and hi-end loot
        (6, 'Healing Encounter') #ust like a trap encounter - but beneficial        
    ]

    event_name = models.CharField(max_length=200)
    event_type = models.IntegerField(choices=EVENT_TYPE, default=0)

    event_event_image = models.ManyToManyField(EventImage, through='EventImage', blank=True, null=True)

    event_AI_description = models.ForeignKey(EventAIDescription, on_delete=models.CASCADE, blank=True, null=True)


class CurrentEvent(models.Model):
    current_event = models.ForeignKey(Event, on_delete=models.CASCADE)

    @property
    def event_name(self):
        return self.current_event.event_name

    @property
    def event_type(self):
        return self.current_event.event_type

    @property
    def event_event_image(self):
        return self.current_event.event_event_image

    @property
    def event_AI_description(self):
        return self.current_event.event_AI_description


class Journey(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    day = models.IntegerField()
    day_visited = models.BooleanField(default=False)
    event = models.ManyToManyField(CurrentEvent, through='CurrentEventInJourney')
    next_day = models.ForeignKey("Journey", on_delete=models.SET_NULL, null=True, related_name='prev')

    def generate_event(self):
        event_list = Event.objects.all()
        ce = choice(event_list)
        current_event_ = CurrentEvent.objects.create(current_event=ce)
        CurrentEventInJourney.objects.create(journey=self, event=current_event_)


class CurrentEventInJourney(models.Model):
    event = models.ForeignKey(CurrentEvent, on_delete=models.CASCADE)
    journey = models.ForeignKey(Journey, on_delete=models.CASCADE)


class AliveMonster(models.Model):
    monster_class = models.ForeignKey(Monster, on_delete=models.CASCADE)
    current_hp = models.IntegerField(null=True)

    # current_attack = models.IntegerField(null=True)
    # current_defence = models.IntegerField(null=True)

    @property
    def monsters_gold(self):
        return self.monster_class.monsters_gold

    @property
    def attack(self):
        return self.monster_class.attack

    @property
    def defence(self):
        return self.monster_class.defence

    @property
    def name(self):
        return self.monster_class.name

    @property
    def description(self):
        return self.monster_class.description

    @property
    def monster_image(self):
        return self.monster_class.monster_monster_image


class Stage(models.Model):

    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    monsters = models.ManyToManyField(AliveMonster, through='AliveMonsterInStage')
    visited = models.BooleanField(default=False)
    #next_stage = models.ForeignKey("Stage", on_delete=models.SET_NULL, null=True, related_name='prev')

    def generate_monster(self):
        monster_list = Monster.objects.all()
        amount = randint(1, 1) #for now only one monster to defeat
        for _ in range(amount):
            mc = choice(monster_list)
            extra_hp = randint(-5, 5)
            am = AliveMonster.objects.create(monster_class=mc, current_hp=mc.hp + extra_hp)
            AliveMonsterInStage.objects.create(stage=self, monster=am)


class AliveMonsterInStage(models.Model):
    monster = models.ForeignKey(AliveMonster, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    
    """
class Journal(models.Model):
    day_number = models.IntegerField(default=0)
    day_event = models.ForeignKey(Journey, on_delete=models.CASCADE)
    day_event_fight = models.ForeignKey(Stage, on_delete=models.CASCADE)
    day_description = models.TextField(max_length=500, blank=True)
    
    def add_journal_entry(self):
        pass #method for the journal? Hmm"""
    

class Comment(models.Model):
    comment = models.TextField(max_length = 1000)

"""
class JourneyEntry(models.Model):
    hero = models.CharField(max_length=100)
    day = models.IntegerField()
    event_type = models.CharField(max_length=100)
    #day_description_original = models.TextField(max_length=1000, blank=True)
    #day_description_by_AI = models.TextField(max_length=100, blank=True)


class FightEntry(models.Model):
    hero = models.CharField(max_length=100)
    monster = models.CharField(max_length=100)
    fight_description_original = models.TextField(max_length=1000, blank=True)
    fight_description_by_AI = models.TextField(max_length=100, blank=True)
"""

