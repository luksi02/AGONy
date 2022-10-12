from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views import View
from random import shuffle
from django.core.paginator import Paginator
from django.http import HttpResponse
import openai, os
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView

from AGONy.models import Hero, Monster, Stage, Event, Origin  # Game
from AGONy.forms import HeroCreateForm, MonsterCreateForm, CreateUserForm, LoginForm, OriginCreateForm, EventCreateForm
from rpg.models import Game


# Create your views here.
def agony(request):
    openai.api_key = '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'  # os.getenv("OPENAI_API_KEY")
    # OPEN_API_KEY = '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'
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
    """
    Backstory created by AI based on few (checkbox?) (or many CausesForAGONy
    (database with tragic/racial/classical/other orgins)
    """

    message = """
    Create Hero, so he/she can bravely march into oblivion! Yyy, glory and power, of course.
    Anyway, this Hero is going to be yours eyes and ears, so be serious about your creation!
    """

    model = Hero
    fields = ['name', 'race']
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


class HeroesInAgonyList(ListView):
    message = """
    List of bold, ambitious Heroes awaiting for your command to march into oblivion! Yyy. yes, yes, glory and power, yes.
    """

    model = Hero
    template_name = 'agony_hero_list.html'


class MyHeroesInAgonyList(LoginRequiredMixin, ListView):
    message = """
    List of bold, ambitious Heroes awaiting for your command to march into oblivion! Yyy. yes, yes, glory and power, yes.
    """

    model = Hero
    template_name = 'agony_hero_list.html'


class UpdateHeroInAgony(LoginRequiredMixin, UpdateView):
    """
    For now, I think only option to modify will be wielding/changing equipped another armor/weapon
    """

    message = """
    Go on, put your Hero in more AGONy! Do it today, don't wait for tomorrow!. They're made up, who cares what happen to them?
    """

    model = Hero
    form_class = HeroCreateForm
    template_name = 'agony_form.html'
    success_url = reverse_lazy('AGONy_hero_list')


class EndHeroAgony(View):
    """
    hmm, I think I won't let player to delete heroes, only kill them. Their journey must be
    kept for future generations! And for my fun, of course. But mostly, future generations"""

    message = """
    So, you decided to take easy way out of adventure for your Hero..., that's one way to do that. Not best, but who am I to judge?
    """

    def get(self):
        pass


class CreateMonsterInAgony(LoginRequiredMixin, CreateView):
    message = """
    Create Hero, so he/she can bravely march into oblivion! Yyy, create a monster for your Hero
    to fight with, so your Hero can find his glory and power!
    Anyway, just create that monster!
    """

    model = Monster
    fields = "__all__"
    template_name = 'agony_form.html'
    success_url = reverse_lazy('AGONy_index')


class MonstersInAgonyList(ListView):
    message = """
    Let's see what wonderful creatures await us! Wait, why did it bite my leg off? 
    Is this blood? Get a cleric, quick!
    """

    model = Monster
    template_name = 'agony_monster_list.html'


class UpdateMonsterInAgony(LoginRequiredMixin, UpdateView):
    message = """
    Let's add a horn, or two, maybe chainsaw or some tentacles to this monster!
    """

    model = Monster
    form_class = MonsterCreateForm
    template_name = 'agony_form.html'
    success_url = reverse_lazy('AGONy_monster_list')


class CreateOriginOfAgony():
    message = """
    Why not, tell us what happend in your hero past so he felt call for adventure!
    """

    model = Origin
    fields = "__all__"
    template_name = 'agony_form.html'
    success_url = reverse_lazy('AGONy_index')


class OriginsOfAgonyList(ListView):
    message = """
    """

    model = Origin
    template_name = 'agony_monster_list.html'


class UpdateOriginOfAgony(LoginRequiredMixin, UpdateView):
    message = """
    """

    model = Origin
    form_class = OriginCreateForm
    template_name = 'agony_form.html'
    success_url = reverse_lazy('AGONy_monster_list')


class CreateEventInAgony():
    message = """
    """

    model = Event
    fields = "__all__"
    template_name = 'agony_form.html'
    success_url = reverse_lazy('AGONy_index')


class EventsInAgonyList(ListView):
    message = """
    """

    model = Origin
    template_name = 'agony_monster_list.html'


class UpdateEventInAgony(LoginRequiredMixin, UpdateView):
    message = """
    """

    model = Event
    form_class = EventCreateForm
    template_name = 'agony_form.html'
    success_url = reverse_lazy('AGONy_monster_list')


class CreateDefaultsInAgony(View):
    message = """
    Let's just create some defaults for you to play already, who wants to go through boring creating the world?
    """

    def get(self, request):
        # A view to create some defaults in game!
        Hero.objects.create(name='Percy McPerson', race=0)
        Hero.objects.create(name='Woody Oakson', race=1)
        Hero.objects.create(name='Shorty MacBeard', race=2)

        # human-like monsters
        Monster.objects.create(name='Goblin', hp=20, attack=2, defence=1, monster_level=0, monster_type=0)
        Monster.objects.create(name='Orc', hp=40, attack=4, defence=4, monster_level=1, monster_type=0)
        Monster.objects.create(name='Goblin Wolf Rider', hp=50, attack=7, defence=4, monster_level=2, monster_type=0)
        Monster.objects.create(name='Troll', hp=80, attack=8, defence=2, monster_level=3, monster_type=0)
        Monster.objects.create(name='Giant', hp=200, attack=15, defence=5, monster_level=4, monster_type=0)

        # wild-wild-life monsters
        Monster.objects.create(name='Wolf', hp=25, attack=3, defence=0, monster_level=0, monster_type=1)
        Monster.objects.create(name='Giant Venomous Spider', hp=50, attack=5, defence=2, monster_level=1,
                               monster_type=1)
        Monster.objects.create(name='Angry Bear', hp=80, attack=7, defence=7, monster_level=2, monster_type=1)
        Monster.objects.create(name='Fancy Unicorn', hp=100, attack=6, defence=6, monster_level=3, monster_type=1)
        Monster.objects.create(name='Dragon', hp=150, attack=10, defence=10, monster_level=4, monster_type=1)

        # undead monsters
        Monster.objects.create(name='Zombie', hp=40, attack=2, defence=0, monster_level=0, monster_type=2)
        Monster.objects.create(name='Skeleton', hp=55, attack=3, defence=3, monster_level=1, monster_type=2)
        Monster.objects.create(name='Skeleton Archer', hp=60, attack=6, defence=6, monster_level=2, monster_type=2)
        Monster.objects.create(name='Lich', hp=80, attack=15, defence=3, monster_level=3, monster_type=2)
        Monster.objects.create(name='Vampire', hp=125, attack=6, defence=15, monster_level=4, monster_type=2)

        # origins - general
        Origin.objects.create(origin_type=0, origin_description="Tired of mundane life, felt call for adventure")
        Origin.objects.create(origin_type=0, origin_description="Want to get rich fast, or die trying")
        Origin.objects.create(origin_type=0, origin_description="Got lured to adventure by songs of riches and glory")
        Origin.objects.create(origin_type=0, origin_description="Broke the law, it's desperate try to clear name")

        # origins - tragic
        Origin.objects.create(origin_type=0,
                              origin_description="Got his family murdered, now on a quest to avenge them!")
        Origin.objects.create(origin_type=0,
                              origin_description="Murdered a lot of people, now running away from law enforcement!")
        Origin.objects.create(origin_type=0, origin_description="Got set up in criminal activity, it's a way to repent")

        # default user creation
        User.objects.create(username='abc', password1='12345678', password2='12345678')
        User.objects.create(username='xyz', password1='12345678', password2='12345678')

        # event
        Event.objects.create(type=0, name="Your Hero encountered Monster, now stand and fight it!")
        Event.objects.create(type=1, name="Ooh, shiney! You found something!")
        Event.objects.create(type=2, name="Crap, it's a trap!")
        Event.objects.create(type=3, name="Wonderful views, aren't they? So beautiful landscape!")

        return redirect('AGONy_index')


class CreateUserView(View):
    message = """
    Create User - then you can play, maybe even leave a comment what to improve in my game? Be sure to subscribe!
    """

    def get(self, request):
        form = CreateUserForm()
        return render(request, 'agony_form.html', {'form': form})

    def post(self, request):
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save(
                commit=False)

            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            return redirect('AGONy_index')
        return render(request, 'agony_form.html', {'form': form})


class LoginView(View):
    message = """
    Login your user, play & comment. Have a nice day! 
    """

    def get(self, request):
        form = LoginForm()
        return render(request, 'agony_form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            us = form.cleaned_data['username']
            pd = form.cleaned_data['password']
            user = authenticate(username=us, password=pd)
            if user is None:
                return render(request, 'agony_form.html', {'form': form, 'message': "Invalid data!"})
            else:
                login(request, user)
                url = request.GET.get('next', 'AGONy_index')
                return redirect(url)
        return render(request, 'agony_form.html', {'form': form, 'message': "Invalid data!"})


class LogoutView(View):
    message = """
    See you later, alligator!
    (prompt: you should answer: after while crocodile!)
    """

    def get(self, request):
        logout(request)
        return redirect('AGONy_index')


class CreateGameForHero(LoginRequiredMixin, View):  # WIP

    def get(self, request, id_hero):
        hero = Hero.objects.get(pk=id_hero)
        stage = Stage.objects.create(level=1)
        stage = Stage.objects.create(next_stage=stage)
        #url = reverse('AGONy_stage_detail', args=(stage.id,))
        url = reverse('AGONy_index')

        return redirect(url)


class StageDetailView(LoginRequiredMixin, View):

    def get(self, request, pk):

        stage = get_object_or_404(Stage, pk=pk)

        if stage.next_stage is None:
            stage.next_stage = Stage.objects.create(level=stage.level + 1)

        if not stage.visited:
            stage.generate_monster()
            stage.visited = True
            stage.save()

        return render(request, 'agony_stage_detail.html', {'stage': stage})