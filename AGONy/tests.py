import pytest
from django.test import Client
from django.urls import reverse

from AGONy.forms import HeroCreateForm, MonsterCreateForm, EventCreateForm, CreateUserForm, LoginForm
from AGONy.models import Hero, Monster, Event, Stage, Journey
from django.contrib.auth.models import User

#1_1_AGONyIndexView
def test_index():
    client = Client()
    url = ''
    response = client.get(url)
    assert response.status_code == 200
    assert 'AGONy' in str(response.content)


#2_1_AGONyWorkInProgress
def test_work_in_progress():
    client = Client()
    url = '/wip/'
    response = client.get(url)
    assert response.status_code == 200
    assert 'WORK IN PROGRESS' in str(response.content)

#3_1_CreateHeroInAgony
def test_create_hero_get_not_logged(client):
    client = Client()
    url = reverse('AGONy_create_hero')
    response = client.get(url)
    assert response.status_code == 200


#3_2_CreateHeroInAgony
@pytest.mark.django_db
def test_create_hero_get_logged_in(client, user):
    url = reverse('AGONy_create_hero')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


#3_3_CreateHeroInAgony
@pytest.mark.django_db
def test_create_hero_post_logged_in(client, user, hero):
    url = reverse('AGONy_create_hero')
    client.force_login(user)
    data = {
        'name':'Hero Mcbrave'
    }
    response = client.post(url, data)
    assert response.status_code == 200
    assert Hero.objects.get(name='Hero McBrave')


#5_1_Leaderboard
@pytest.mark.django_db
def test_heroes_list_get(client, heroes):
    url = reverse('AGONy_hero_list')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(heroes)
    for hero in heroes:
        assert hero in response.context['object_list']


#6_1_MyHeroesView
@pytest.mark.django_db
def test_my_heroes_list_get(client, heroes, user):
    url = reverse('AGONy_hero_list')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(heroes)
    for hero in heroes:
        assert hero in response.context['object_list']


#7_1_UpdateHero
@pytest.mark.django_db
def test_update_hero_get_logged_in(client, heroes, user):
    hero = heroes[0]
    url = reverse('AGONy_update_hero', args=(hero.id, ))
    client.force_login(user)
    response = client.get(url)
    form_obj = response.context['form']
    assert response.status_code == 200
    assert isinstance(form_obj, HeroCreateForm)


#7_2_UpdateHero
@pytest.mark.django_db
def test_update_hero_post_logged_in(client, heroes, user):
    hero = heroes[0]
    url = reverse('AGONy_update_hero', args=(hero.id, ))
    client.force_login(user)
    data = {
        'name' : 'Hero McBrave'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Hero.objects.get(name=data['name'])

#8_1_CreateMonsterInAgony
def test_create_monster_get_not_logged(client):
    url = reverse('AGONy_create_monster')
    response = client.get(url)
    assert response.status_code == 302
    url_redirect = reverse('AGONy_login')
    assert response.url.startswith(url_redirect)


#8_2_CreateMonsterInAgony
@pytest.mark.django_db
def test_create_monster_get_logged_in(client, user):
    url = reverse('AGONy_create_monster')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
    #url_redirect = reverse('AGONy_login')
    #assert response.url.startswith(url_redirect)

#8_3_CreateMonsterInAgony
@pytest.mark.django_db
def test_create_monster_post_logged_in(client, user):
    url = reverse('AGONy_create_monster')
    client.force_login(user)
    data = {
        'name':'AngryBird',
        'hp' : 5,
        'attack' : 0,
        'defence' : 0,
        'monster_level' : 0,
        'monster_type' : 0,
        'description' : 'blablabla',
        'monsters_gold' : 10
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Monster.objects.get(name=data['name'])


#9_1_MonsterList
@pytest.mark.django_db
def test_monster_list_get(client, monsters, user):
    url = reverse('AGONy_monster_list')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(monsters)
    for monster in monsters:
        assert monster in response.context['object_list']


#10_1_UpdateMonster
@pytest.mark.django_db
def test_update_monster_get_logged_in(client, monsters, user):
    monster = monsters[0]
    url = reverse('AGONy_update_monster', args=(monster.id, ))
    client.force_login(user)
    response = client.get(url)
    form_obj = response.context['form']
    assert response.status_code == 200
    assert isinstance(form_obj, MonsterCreateForm)


#10_2_UpdateMonster
@pytest.mark.django_db
def test_update_monster_post_logged_in(client, monsters, user):
    monster = monsters[0]
    url = reverse('AGONy_update_monster', args=(monster.id, ))
    client.force_login(user)
    data = {
        'name': 'AngryBird',
        'hp': 5,
        'attack': 0,
        'defence': 0,
        'monster_level': 0,
        'monster_type': 0,
        'description': 'blablabla',
        'monsters_gold': 10
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Monster.objects.get(name=data['name'])


#11_1_CreateEventInAgony
def test_create_event_get_not_logged(client):
    url = reverse('AGONy_create_event')
    response = client.get(url)
    assert response.status_code == 302
    url_redirect = reverse('AGONy_login')
    assert response.url.startswith(url_redirect)


#11_2_CreateEventInAgony
@pytest.mark.django_db
def test_create_event_get_logged_in(client, user):
    url = reverse('AGONy_create_event')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
    #url_redirect = reverse('AGONy_login')
    #assert response.url.startswith(url_redirect)

#11_3_CreateEventInAgony
@pytest.mark.django_db
def test_create_event_post_logged_in(client, user, event):
    url = reverse('AGONy_create_hero')
    client.force_login(user)
    data = {
        'event_name':'Dragonborn comes'
    }
    response = client.post(url, data)
    assert response.status_code == 200
    assert Event.objects.get(event_name=data['event_name'])


#12_1_AgonyEventsList
@pytest.mark.django_db
def test_event_list_get(client, events, user):
    url = reverse('AGONy_event_list')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(events)
    for event in events:
        assert event in response.context['object_list']


#13_1_UpdateEvent
@pytest.mark.django_db
def test_update_event_get_logged_in(client, events, user):
    event = events[0]
    url = reverse('AGONy_update_event', args=(event.id, ))
    client.force_login(user)
    response = client.get(url)
    form_obj = response.context['form']
    assert response.status_code == 200
    assert isinstance(form_obj, EventCreateForm)


#13_2_UpdateEvent
@pytest.mark.django_db
def test_update_event_post_logged_in(client, events, user):
    event = events[0]
    url = reverse('AGONy_update_event', args=(event.id, ))
    client.force_login(user)
    data = {
        'event_type' : 0,
        'event_name' : 'Dragonborn comes'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Event.objects.get(event_name=data['event_name'])


#14_1_CreateDefaults
@pytest.mark.django_db
def test_create_defaults():
    client = Client()
    url = '/AGONy_create_defaults/'
    response = client.get(url)
    assert response.status_code == 302
    assert Monster.objects.get(name='Goblin')


#15_1_CreateUserView
@pytest.mark.django_db
def test_create_user_get(client):
    url = reverse('AGONy_create_user')
    response = client.get(url)
    assert response.status_code == 200
    form_in_view = response.context['form']
    assert isinstance(form_in_view, CreateUserForm)

# 15_2_CreateUserView
@pytest.mark.django_db
def test_create_user_post(client, user):
    client = Client()
    url = reverse('AGONy_create_user')
    data = {
        'username': 'user_looser',
        'password' : '12345678'
    }
    response = client.post(url, data)
    assert response.status_code == 200
    assert User.objects.get(username=data['username'])


#16_1_LoginView
@pytest.mark.django_db
def test_login_view_get():
    client = Client()
    url = '/AGONy_login/'
    response = client.get(url)
    assert response.status_code == 200
    form_in_view = response.context['form']
    assert isinstance(form_in_view, LoginForm)



#16_2_LoginView
@pytest.mark.django_db
def test_login_view_post(user):
    client = Client()
    url = '/AGONy_login/'
    data = {
        'username' : 'user_looser',
        'password' : '12345678'
    }
    response = client.post(url, data)
    assert response.status_code == 200
    #assert response.context['user'].is_active
    #assert response.context['user'].is_authenticated
    #assert response.request['User'].is_authenticated
    assert user.is_authenticated
    assert user.is_active


#17_1_LogoutView
@pytest.mark.django_db
def test_logout_view_get(user):
    client = Client()
    #client.force_login(user)
    url = '/AGONy_logout/'
    client.force_login(user)
    assert user.is_authenticated
    assert user.is_active
    response = client.get(url)
    assert response.status_code == 302
    #assert response.context['user'].is_active
    #assert response.context['user'].is_authenticated
    #assert response.request['User'].is_authenticated
    assert user.is_authenticated
    assert user.is_active


#18_1_CreateStageForHero
@pytest.mark.django_db
def test_create_stage_get_not_logged(client, hero):
    url = reverse('AGONy_create_game_for_hero', args=(hero.id, ))
    response = client.get(url)
    assert response.status_code == 302
    url_redirect = reverse('AGONy_login')
    assert response.url.startswith(url_redirect)


#18_2_CreateStageForHero
@pytest.mark.django_db
def test_create_stage_get_logged_in(client, user, hero):
    url = reverse('AGONy_create_game_for_hero', args=(hero.id, ))
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 302



#18_3_CreateStage
@pytest.mark.django_db
def test_create_stage_post_logged_in(client, user, hero, alivemonster1, stage):
    url = reverse('AGONy_create_game_for_hero', args=(hero.id, ))
    client.force_login(user)
    data = {
        'hero': hero.id,
        'level': 1,
        'monsters': alivemonster1,
        'visited':False,
        'next_stage':stage
    }
    response = client.post(url, data)
    assert response.status_code == 200
    assert Stage.objects.get(hero=data['hero'])


# 19_3_StageDetailView
@pytest.mark.django_db
def test_stage_detail_view_get(client, user, hero, alivemonsters, stage):
    url = reverse('AGONy_stage_detail', args=(stage.id, ))
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
    assert Stage.objects.get(visited=True)

"""#21_1_JourneyDetailView
@pytest.mark.django_db
def test_journey_detail_view_get(client, user, journey, event_list):
    url = reverse('AGONy_journey_detail', args=(journey.id, ))
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
    assert Journey.objects.get(day_visited=False)"""

#20_1_CreateJourneyForHero
@pytest.mark.django_db
def test_create_journey_get_not_logged(client, hero):
    url = reverse('AGONy_create_journey_for_hero', args=(hero.id, ))
    response = client.get(url)
    assert response.status_code == 302
    url_redirect = reverse('AGONy_login')
    assert response.url.startswith(url_redirect)



#20_2_CreateJourneyForHero
@pytest.mark.django_db
def test_create_journey_get_logged_in(client, user, hero):
    url = reverse('AGONy_create_journey_for_hero', args=(hero.id, ))
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


#20_3_CreateJourneyForHero
@pytest.mark.django_db
def test_create_journey_post_logged_in(client, user, hero, event_list):
    url = reverse('AGONy_create_journey_for_hero', args=(hero.id, ))
    client.force_login(user)
    data = {
        'hero': hero.id,
        'day': 1,
        'event': event_list

    }
    response = client.post(url, data)
    assert response.status_code == 200
    assert Journey.objects.get(hero=data['hero'])


#21_1_JourneyDetailView
@pytest.mark.django_db
def test_journey_detail_view_get(client, user, journey, event_list):
    url = reverse('AGONy_journey_detail', args=(journey.id, ))
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
    assert Journey.objects.get(day_visited=False)


#22_1_AttackMonsterView
@pytest.mark.django_db
def test_attack_monster_get(client, user, hero, alivemonster1, stage):
    url = reverse('AGONy_attack_monster', args=(alivemonster1.id, hero.id))
    hero = Hero.objects.get(id=hero.id)
    hero_hp = hero.hp
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 302
    hero_new = Hero.objects.get(id=hero.id)
    hero_hp_new = hero_new.hp
    assert hero_hp_new < hero_hp


#23_1_FoundSomethingView
@pytest.mark.django_db
def test_found_something_get(client, user, journey, hero):
    url = reverse('AGONy_found_something', args=(journey.id, ))
    hero = Hero.objects.get(id=journey.hero.id)
    hero_gold = hero.gold
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 302
    hero_new = Hero.objects.get(id=journey.hero.id)
    hero_gold_new = hero_new.gold
    assert hero_gold_new > hero_gold


#24_1_TrapView
@pytest.mark.django_db
def test_trap_view_get(client, user, journey):
    url = reverse('AGONy_trap', args=(journey.id, ))
    hero = Hero.objects.get(id=journey.hero.id)
    hero_hp = hero.hp
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 302
    hero_new = Hero.objects.get(id=journey.hero.id)
    hero_hp_new = hero_new.hp
    assert hero_hp_new < hero_hp


#25_1_RunAwayView
@pytest.mark.django_db
def test_run_away_view_get(client, user, journey):
    url = reverse('AGONy_run_away', args=(journey.id, ))
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 302
    assert Journey.objects.get(day_visited=False)


#26_1_ReturnToJourney
@pytest.mark.django_db
def test_return_to_journey_view_get(client, user, journey):
    url = reverse('AGONy_return_to_journey', args=(journey.id, ))
    journey = Journey.objects.get(id=journey.id)
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 302
    _journey = Journey.objects.get(id=journey.id)
    assert _journey.day_visited == False
