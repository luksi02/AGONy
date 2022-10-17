from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views import View
from random import shuffle, choice
from django.core.paginator import Paginator
from django.http import HttpResponse
import openai, os
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView

from AGONy.models import Hero, Monster, Stage, Event, Origin, AliveMonster, Journey #Game,
from AGONy.forms import HeroCreateForm, MonsterCreateForm, CreateUserForm, LoginForm, OriginCreateForm, EventCreateForm


def agony(request):
    openai.api_key = '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'  # os.getenv("OPENAI_API_KEY")
    OPEN_API_KEY = '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'
    absurd = """when they entered cave, the dragon was masturbating using goblin midget in smurf costume as a toy"""
    query_text = """a prayer to a machinegod: From the moment I understood the weakness of my flesh, it disgusted me.
    I craved the strength and certainty of steel. I aspired to the purity of the blessed machine.
Your kind cling to your flesh as if it will not decay and fail you. One day the crude biomass you call a temple will wither and you will beg my kind to save you.
But I am already saved. For the Machine is Immortal."""
    query_text1 = "Origin story of a dwarf that lived under dungeon stronhold in shadowy Blue Mountains"
    query_response = openai.Completion.create(engine="davinci-instruct-beta", prompt=absurd, temperature=0,
                                              max_tokens=500, top_p=1, frequency_penalty=0, presence_penalty=0)
    print(query_response.choices[0].text.split('.'))
    return HttpResponse(query_response.choices[0].text.split('.'))


class CreateGameForHero(LoginRequiredMixin, View):

    def get(self, request, id_hero):
        hero = Hero.objects.get(pk=id_hero)
        stage = Stage.objects.create(hero=hero, level=1)
        stage = Stage.objects.create(hero=hero, next_stage=stage)
        url = reverse('AGONy_stage_detail', args=(stage.id,))
        return redirect(url)


class StageDetailView(LoginRequiredMixin, View):

    def get(self, request, pk):

        context = """There's something in the distance, is it a bird?
         Is it a plane? Oh shit, it's a monster, an angry monster!"""

        stage = get_object_or_404(Stage, pk=pk)

        if stage.next_stage is None:
            stage.next_stage = Stage.objects.create(level=stage.level + 1)

        if not stage.visited:
            stage.generate_monster()
            stage.visited = True
            stage.save()

        return render(request, 'agony_stage_detail.html', {'stage': stage, 'context': context})


class CreateJourneyForHero(LoginRequiredMixin, View):

    def get(self, request, id_hero):
        hero = Hero.objects.get(pk=id_hero)
        journey = Journey.objects.create(hero=hero, day=1)
        #journey_next_day = Stage.objects.create(hero=hero, next_day=journey)
        url = reverse('AGONy_journey_detail', args=(journey.id,))
        return redirect(url)


class JourneyDetailView(LoginRequiredMixin, View):

    def get(self, request, pk):

        context = """What a beautiful day! Something happens, let's see what:"""

        journey = get_object_or_404(Journey, pk=pk)

        #if journey.next_stage is None:
        #    stage.next_stage = Stage.objects.create(level=stage.level + 1)

        if not journey.day_visited:
            journey.generate_event()
            journey.day_visited = True
            journey.save()

        return render(request, 'agony_journey_detail.html', {'journey': journey, 'context': context})
"""class FightView(LoginRequiredMixin, View):
    def get(self, request, stage_id):
        stage = Stage.objects.get(pk=stage_id)
        monsters = stage.monsters.filter(current_hp__gt=0)
        hero = stage.game.hero
        if monsters.count() > 0:
            target = choice(monsters)
            dm = hero.attack - target.defence
            if dm <= 0:
                dm = 1
            target.current_hp -= dm
            target.save()
            monster_dmg = 0
            for monster in monsters:
                dm = monster.attack - hero.defence
                if dm <= 0:
                    dm = 1
                monster_dmg += dm
            hero.hp -= dm
            hero.save()
        url = reverse('AGONy_stage_detail', args=(stage_id,))
        return redirect(url)"""


class AttackMonsterView(View):

    def get(self, request, monster_id, hero_id):
        monster = AliveMonster.objects.get(pk=monster_id)
        hero = Hero.objects.get(pk=hero_id)
        dmg = hero.attack - monster.defence
        if dmg <= 0:
            dmg = 1
        monster.current_hp -= dmg
        monster.save()
        if monster.current_hp > 0:
            dmg = monster.attack - hero.defence
            if dmg <= 0:
                dmg = 1
            hero.hp -= dmg
        else:
            hero.gold += monster.monsters_gold
        hero.save()
        stage = monster.stage_set.first()
        return redirect('AGONy_stage_detail', stage.id)


