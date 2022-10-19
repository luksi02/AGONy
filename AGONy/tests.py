import pytest
from django.test import Client
from django.urls import reverse

from AGONy.forms import HeroCreateForm, MonsterCreateForm
from AGONy.models import Hero, Monster #, Game

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
    url = reverse('AGONy_create_hero')
    response = client.get(url)
    assert response.status_code == 200
    url_redirect = reverse('AGONy_login')    #redirect bo nie zalogowany
    assert response.url.startswith(url_redirect)


#3_2_CreateHeroInAgony
@pytest.mark.django_db
def test_create_hero_get_logged_in(client, user):
    url = reverse('AGONy_create_hero')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
    url_redirect = reverse('AGONy_login')
    assert response.url.startswith(url_redirect)

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
    url_redirect = reverse('AGONy_login')    #redirect bo nie zalogowany
    assert response.url.startswith(url_redirect)


#8_2_CreateMonsterInAgony
@pytest.mark.django_db
def test_create_monster_get_logged_in(client, user):
    url = reverse('AGONy_create_monster')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
    url_redirect = reverse('AGONy_login')
    assert response.url.startswith(url_redirect)

#8_3_CreateMonsterInAgony
@pytest.mark.django_db
def test_create_monster_post_logged_in(client, user, monster):
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
    assert Monster.objects.get(name=data['name'], description=data['description'])


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
"""def test_create_hero_get_not_logged(client):
    url = reverse('AGONy_create_hero')
    response = client.get(url)
    assert response.status_code == 200
    url_redirect = reverse('AGONy_login')    #redirect bo nie zalogowany
    assert response.url.startswith(url_redirect)"""


#11_2_CreateEventInAgony
"""@pytest.mark.django_db
def test_create_hero_get_logged_in(client, user):
    url = reverse('AGONy_create_hero')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
    url_redirect = reverse('AGONy_login')
    assert response.url.startswith(url_redirect)"""

#11_3_CreateHeroInAgony
"""@pytest.mark.django_db
def test_create_hero_post_logged_in(client, user, hero):
    url = reverse('AGONy_create_hero')
    client.force_login(user)
    data = {
        'name':'Hero Mcbrave'
    }
    response = client.post(url, data)
    assert response.status_code == 200
    assert Hero.objects.get(name='Hero McBrave')"""


#12_1_AgonyEventsList
"""@pytest.mark.django_db
def test_my_heroes_list_get(client, heroes, user):
    url = reverse('AGONy_hero_list')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(heroes)
    for hero in heroes:
        assert hero in response.context['object_list']"""


#13_1_UpdateEvent
"""@pytest.mark.django_db
def test_update_hero_get_logged_in(client, heroes, user):
    hero = heroes[0]
    url = reverse('AGONy_update_hero', args=(hero.id, ))
    client.force_login(user)
    response = client.get(url)
    form_obj = response.context['form']
    assert response.status_code == 200
    assert isinstance(form_obj, HeroCreateForm)"""


#13_2_UpdateEvent
"""@pytest.mark.django_db
def test_update_hero_post_logged_in(client, heroes, user):
    hero = heroes[0]
    url = reverse('AGONy_update_hero', args=(hero.id, ))
    client.force_login(user)
    data = {
        'name' : 'Hero McBrave'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Hero.objects.get(name=data['name'])"""

#14_1_CreateDefaults

#15_1_CreateUserView

#15_2_CreateUserView

#16_1_LoginView

#17_1_LogoutView