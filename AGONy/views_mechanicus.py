from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views import View
from random import shuffle, choice, randint
from django.core.paginator import Paginator
from django.http import HttpResponse
import openai, os
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
#from transformers import pipeline

from AGONy.models import Hero, Monster, Stage, Event, Origin, AliveMonster, Journey #Game,
from AGONy.forms import HeroCreateForm, MonsterCreateForm, CreateUserForm, LoginForm, OriginCreateForm, EventCreateForm


def agony(request):
    openai.api_key = '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'  # os.getenv("OPENAI_API_KEY")
    OPEN_API_KEY = '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'
    absurd = """What a beautiful day! Something happens, let's see what: Brave hero journeys into unknown. 
    Then the magic happens. Hero encounters a big, angry dragon"""
        #"when they entered cave, the dragon was masturbating using goblin midget in smurf costume as a toy"
    query_text = "a prayer to a machinegod: From the moment I understood"
    query_text1 = "Origin story of a dwarf that lived under dungeon stronhold in shadowy Blue Mountains"
    query_response = openai.Completion.create(engine="davinci-instruct-beta", prompt=absurd, temperature=0,
                                              max_tokens=100, top_p=1, frequency_penalty=0, presence_penalty=0)
    print(query_response.choices[0].text.split('.'))
    return HttpResponse(query_response.choices[0].text.split('.'))


def agony2(request):

    absurd = "when they entered cave, the dragon was masturbating using goblin midget in smurf costume as a toy"

    query_text1 = "Origin story of a dwarf that lived under dungeon stronhold in shadowy Blue Mountains"
    generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')
    generated_text = generator(absurd, do_sample=True, min_length=300)
    return HttpResponse(generated_text)


def agony3(request, input_text):
    openai.api_key = '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'  # os.getenv("OPENAI_API_KEY")

    query_response = openai.Completion.create(engine="davinci-instruct-beta", prompt=input_text, temperature=0,
                                              max_tokens=100, top_p=1, frequency_penalty=0, presence_penalty=0)

    print(query_response.choices[0].text.split('.'))

    input_text = "Origin story of a dwarf that lived under dungeon stronhold in shadowy Blue Mountains"

    answer = query_response.choices[0].text.split('.')
    return answer


class CreateGameForHero(LoginRequiredMixin, View):

    def get(self, request, id_hero):
        hero = Hero.objects.get(pk=id_hero)
        stage = Stage.objects.create(hero=hero, level=1)
        #stage = Stage.objects.create(hero=hero, next_stage=stage)
        url = reverse('AGONy_stage_detail', args=(stage.id,))
        return redirect(url)


class StageDetailView(LoginRequiredMixin, View):

    def get(self, request, pk):

        context = """There's something in the distance, is it a bird?
         Is it a plane? Oh shit, it's a monster, an angry monster!"""

        stage = get_object_or_404(Stage, pk=pk)

        """if stage.next_stage is None:
            stage.next_stage = Stage.objects.create(level=stage.level + 1)"""

        if not stage.visited:
            stage.generate_monster()
            stage.visited = True
            stage.save()

        return render(request, 'agony_stage_detail.html', {'stage': stage, 'context': context})


class CreateJourneyForHero(LoginRequiredMixin, View):

    def get(self, request, id_hero):
        if len(Event.objects.all()) ==0:
            return HttpResponse("Create Event first!")
        if len(Monster.objects.all()) == 0:
            return HttpResponse("Create Monsters first!")
        try:
            Journey.objects.get(hero=id_hero, day_visited=False)
            url = reverse('AGONy_return_to_journey', args=(id_hero,))
            return redirect(url)
        except ObjectDoesNotExist:
            hero = Hero.objects.get(pk=id_hero)
            journey = Journey.objects.create(hero=hero, day=1)
            # journey_next_day = journey.objects.create(hero=hero, next_day=journey)
            url = reverse('AGONy_journey_detail', args=(journey.id,))
            return redirect(url)

        """else:
            Journey.objects.get(pk=id_hero)
            url = reverse('AGONy_return_to_journey', args=(id_hero,))
            return redirect(url)

        except ObjectDoesNotExist:
            
            
        else:
            url = reverse('AGONy_return_to_journey', args=(id_hero,))
            return redirect(url)

            if Journey.objects.get(pk=id_hero) is None:
            hero = Hero.objects.get(pk=id_hero)
            journey = Journey.objects.create(hero=hero, day=1)
            #journey_next_day = journey.objects.create(hero=hero, next_day=journey)
            url = reverse('AGONy_journey_detail', args=(journey.id, ))
            return redirect(url)
        else:
            url = reverse('AGONy_return_to_journey', args=(id_hero,))
            return redirect(url)"""





class JourneyDetailView(LoginRequiredMixin, View):

    def get(self, request, pk):


        journey = get_object_or_404(Journey, pk=pk)

        if journey.next_day is None:
            journey.next_day = Journey.objects.create(hero=journey.hero, day=journey.day + 1)

        if not journey.day_visited:
            journey.generate_event()

            """if journey.event.event_type == 2:
                journey.hero.hp = journey.hero.hp - randint(5,10)
            if journey.event.event_type == 1:
                journey.hero.hp = journey.hero.gold + randint(5,10)"""
            journey.day_visited = True
            journey.save()

        previous_context = """What a beautiful day! Something happens, let's see what:"""

        input_text = previous_context + "brave hero journeys into unknown. Then the magic happens. Hero encounters a big, angry dragon"

        context = agony3(request, input_text) # + journey.event.event_name)



        return render(request, 'agony_journey_detail.html', {'journey': journey, 'context': context})


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

class FoundSomething(View):

    def get(self, request, pk):
        journey = Journey.objects.get(pk=pk)
        hero = journey.hero
        added_gold = randint(1, 5)
        hero.gold += added_gold
        hero.save()
        #next_day_id = journey.id()
        url = reverse('AGONy_journey_detail', args=(journey.id, ))
        return redirect(url)


class OhCrapItsATrap(View):

    def get(self, request, pk):
        journey = Journey.objects.get(pk=pk)
        hero = journey.hero
        trap_damage = randint(1, 10)
        hero.hp -= trap_damage
        hero.save()
        #next_day_id = journey.id()
        url = reverse('AGONy_journey_detail', args=(journey.id, ))
        return redirect(url)


class RunAway(View):

    def get(self, request, pk):
        journey = Journey.objects.get(pk=pk)
        hero = journey.hero
        running_chances = randint(0,3)
        if running_chances > 1:
            url = reverse('AGONy_journey_detail', args=(journey.id,))
            return redirect(url)
        unsuccesful_run_damage = randint(1, 10)
        hero.hp -= unsuccesful_run_damage
        hero.save()
        # next_day_id = journey.id()
        url = reverse('AGONy_create_game_for_hero', args=(journey.hero.id,))
        return redirect(url)

class ReturnToJourney(View):

    def get(self, request, pk):
        return_to_journey = Journey.objects.get(hero_id=pk, day_visited=False)
        url = reverse('AGONy_journey_detail', args=(return_to_journey.id,))
        return redirect(url)
    
class NewEntryInJournal(View):
    
    def get(self, request, pk):
        journey = Journey.objects.get(pk=pk)
        hero = journey.hero   # check this!
        day_event_description = f'My dearest diary, on {journey.day} day I, the mighty {journey.hero.name} got into {journey.event_name}. It was a great day!' # maybe later add what was the effect. Or not.
        #maybe put it in every event, as function? It's probalby the best idea.
        
