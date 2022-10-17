import pytest
from django.test import Client
from django.urls import reverse

from AGONy.forms import HeroCreateForm, MonsterCreateForm
from AGONy.models import Hero, Monster #, Game


def test_index():
    client = Client()
    url = ''
    response = client.get(url)
    assert response.status_code == 200
    assert 'AGONy' in str(response.content)


def test_add_hero_get():
    client = Client()  # otwórz przeglądarke
    url = reverse('AGONy_create_hero')  # znajdz url o nazwie AGONy_create_hero
    response = client.get(url)  # wejdz metodą get nasza symulacyjną przegladarka na tego URL
    assert response.status_code == 200
    form_in_view = response.context['form']  # pobierz z kontekstu zmienną o nazwie form
    assert isinstance(form_in_view, HeroCreateForm)

"""
@pytest.mark.django_db  # ten dekorator mowi temu testowi wolno dotykać bazy danych
def test_add_hero_post():
    client = Client()  # otwórz przeglądarke
    url = reverse('AGONy_create_hero')  # znajdz url o nazwie create_hero
    data = {  # wpisz w formularzy w pole name wartość slawek
        'name': 'Lolson',
    }
    response = client.post(url, data)  # wejdz metodą post nasza symulacyjną przegladarka na tego URL
    assert response.status_code == 302  # bo w widoku jest redirect
    assert response.url.startswith(url)
    assert Hero.objects.get(name='Lolson')  # sprawdz czy Lolson jest w bazie danych


@pytest.mark.django_db
def test_all_hero_get(heroes):
    client = Client()
    url = reverse('AGONy_hero_list')
    response = client.get(url)
    assert response.status_code == 200
    heroes_form_view = response.context['heroes']
    assert heroes_form_view.count() == len(heroes)


def test_add_Monster_get():
    client = Client()  # otwórz przeglądarke
    url = reverse('AGONy_create_monster')  # znajdz url o nazwie create_hero
    response = client.get(url)  # wejdz metodą get nasza symulacyjną przegladarka na tego URL
    assert response.status_code == 200
    form_in_view = response.context['form']  # pobierz z kontekstu zmienną o nazwie formularz
    assert isinstance(form_in_view, MonsterCreateForm)


@pytest.mark.django_db  # ten dekorator mowi temu testowi wolno dotykać bazy danych
def test_add_monster_post():
    client = Client()  # otwórz przeglądarke
    url = reverse('AGONy_create_monster')  # znajdz url o nazwie 'AGONy_create_monster'
    data = {  # wpisz w formularzu w pole name wartość Lolek
        'name': 'Lolek',
        'hp': 100,
        'attack': 100,
        'defence': 100,
    }
    response = client.post(url, data)  # wejdz metodą post nasza symulacyjną przegladarka na tego URL
    assert response.status_code == 302  # bo w widoku jest redirect
    assert response.url.startswith(url)
    assert Monster.objects.get(name='Lolek', hp=100, attack=100, defence=100)  # sprawdz czy Lolek jest w bazie danych

"""