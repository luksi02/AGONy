from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views import View
# from .models import Recipe, Plan, RecipePlan, Page
from random import shuffle
from django.core.paginator import Paginator
from django.http import HttpResponse
import openai, os
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView

from AGONy.models import Hero, Monster, Stage # Game
from AGONy.forms import HeroCreateForm, MonsterCreateForm
from rpg.models import Game


# Create your views here.
def agony(request):
    openai.api_key = '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' #os.getenv("OPENAI_API_KEY")
    #OPEN_API_KEY = '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'
    query_text = """a prayer to a machinegod: From the moment I understood the weakness of my flesh, it disgusted me.
    I craved the strength and certainty of steel. I aspired to the purity of the blessed machine.

Your kind cling to your flesh as if it will not decay and fail you. One day the crude biomass you call a temple will wither and you will beg my kind to save you.

But I am already saved. For the Machine is Immortal."""
    query_text1 = "Origin story of a dwarf that lived under dungeon stronhold in shadowy Blue Mountains"
    query_response = openai.Completion.create(engine="davinci-instruct-beta", prompt=query_text, temperature=0,
                                        max_tokens=500, top_p=1, frequency_penalty=0, presence_penalty=0)
    print(query_response.choices[0].text.split('.'))
    return HttpResponse(query_response.choices[0].text.split('.'))

class AGONyIndexView(View):
    """landing page, perhaps large incoming, flaming text 'AGONy: Adventure Generator Of Nonsense journey' """

    def get(self, request):
        return render(request, 'agony_base.html')

class AGONyWorkInProgress(View):
    """landing page, perhaps large incoming, flaming text 'AGONy: Adventure Generator Of Nonsense journey' """

    def get(self, request):
        return render(request, 'agony_work_in_progress.html')

class CreateHeroInAgony(CreateView):
    """create Hero, so he/she can bravely march into oblivion! Yyy, glory and power, of course.

    Backstory created by AI based on few (checkbox?) (or many CausesForAGONy
    (database with tragic/racial/classical/other orgins)"""

    model = Hero
    fields = ['name', 'race']
    template_name = 'agony_form.html'
    success_url = reverse_lazy('AGONy_hero_list')

class HeroesInAgonyList(ListView):

    model = Hero
    template_name = 'agony_hero_list.html'

class UpdateHeroInAgony(UpdateView):

    model = Hero
    form_class = HeroCreateForm
    template_name = 'agony_form.html'
    success_url = reverse_lazy('AGONy_hero_list')


    """
    def get(self, request):
        form = HeroCreateForm()
        return render(request, 'agony_form.html', {'form': form})

    def post(self, request):
        
        form = HeroCreateForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            Hero.objects.create(name=name) #, owner=request.user)
            return redirect('AGONy_index')
        return render(request, 'agony_form.html', {'form': form})

        if form.is_valid():
            form.save()
            return redirect('AGONy_index')
        return render(request, 'agony_form.html', {'form': form})
        """


class CreateMonsterInAgony(CreateView):

    model = Monster
    fields = "__all__"
    template_name = 'agony_form.html'
    success_url = reverse_lazy('AGONy_index')

class MonstersInAgonyList(ListView):

    model = Monster
    template_name = 'agony_monster_list.html'

class UpdateMonsterInAgony(UpdateView):

    model = Monster
    form_class = MonsterCreateForm
    template_name = 'agony_form.html'
    success_url = reverse_lazy('AGONy_monster_list')


class CreateGameForHero(View):

    def get(self, request, id_hero):
        hero = Hero.objects.get(pk=id_hero)  # pobranie bochatera o id id_hero
        #game = Game.objects.create(hero=hero, level=1)
        stage = Stage.objects.create(level=2) #tu wywalilem game=game
        #stage = Stage.objects.create(game=game, next_stage=stage)
        url = reverse('AGONy_stage_detail', args=(stage.id,))
        return redirect(url)



class UpdatePeopleInAgony():
    """Go on, put them in more AGONy! Do it, they're made up, who cares what happen to them?

    For now, I think only option to modify will be wielding/changing equipped another armor/weapon
    """

    def get(self):
        pass

class EndAGONy():
    """So, you decided to take easy way out of adventure...

    hmm, I think I won't let player to delete heroes, only kill them. Their journey must be
    kept for future generations! And for my fun, of course. But mostly, future generations"""

    def get(self):
        pass

class CreateTragicOrigin():
    """why not, tell us what happend in your hero past so he felt call for adventure!"""

    """
    General?
    1. Tired of mundane life, felt call for adventure
    2. Want to get rich fast, or die trying
    3. Got lured to adventure by songs of riches and glory
    4. Broke the law, it's desperate try to clear name
    
    
    """


