import pytest
from django.contrib.auth.models import User

#from django.contrib.auth.models import User

from AGONy.models import Hero, Monster, Event, Stage, Journey, AliveMonster


@pytest.fixture
def heroes():
    lst = []
    for x in range(10):
        lst.append(Hero.objects.create(name=x))
    return lst


@pytest.fixture
def hero():
    return Hero.objects.create(name='Hero McBrave')


@pytest.fixture
def stage(hero):
    return Stage.objects.create(hero=hero)


@pytest.fixture
def journey(hero):
    return Journey.objects.create(hero=hero)

@pytest.fixture
def monsters():
    lst = []
    for x in range(10):
        lst.append(Monster.objects.create(name=x))
    return lst


@pytest.fixture
def monster():
    return Monster.objects.create(name='AngryBird',
                                  hp=5,
                                  attack=0,
                                  defence=0,
                                  monster_level=0,
                                  monster_type=0,
                                  description='blablabla',
                                  monsters_gold=10)


@pytest.fixture
def monster2():
    return Monster.objects.create(name='AngryBird')

@pytest.fixture
def alivemonster(stage, monster):
    return AliveMonster.objects.create(monster=monster, stage=stage)

@pytest.fixture
def events():
    lst = []
    for x in range(10):
        lst.append(Event.objects.create(event_name=x))
    return lst


@pytest.fixture
def event():
    return Event.objects.create(event_name='Dragonborn comes')


@pytest.fixture
def user():
    return User.objects.create(username='user_looser', password='12345678')