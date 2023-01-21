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
from django.views.generic import CreateView, ListView, UpdateView, DetailView

from AGONy.models import Hero, Monster, Stage, Event, Origin, Comment, MonsterImage #, Game
from AGONy.forms import HeroCreateForm, MonsterCreateForm, CreateUserForm, LoginForm, OriginCreateForm, EventCreateForm




class AGONyIndexView(View):
    """landing page, perhaps large incoming, flaming text 'AGONy: Adventure Generator Of Nonsense journey' """

    def get(self, request):


        message = "Welcome adventurer, begin jour journey!"
        return render(request, 'agony_base.html', {'message' : message})


class AGONyWorkInProgress(View):
    """landing page, perhaps large incoming, flaming text 'AGONy: Adventure Generator Of Nonsense journey' """

    def get(self, request):
        return render(request, 'agony_work_in_progress.html')


class ContactView(View):
    """"""

    def get(self, request):
        return render(request, 'agony_contact.html')

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


class Leaderboard(View):   #Leaderboard

    def get(self, request):

        message = """
        List of bold, ambitious Heroes that took up the quest for power and glory!
        """

        object_list = Hero.objects.order_by('-gold')
        return render(request, 'agony_leaderboard.html', {'object_list' : object_list, 'message' : message})


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
    success_url = reverse_lazy('AGONy_my_hero_list')


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


class MonstersInAgonyList(LoginRequiredMixin, ListView):
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


class DetailMonsterInAgony(LoginRequiredMixin, DetailView):
    message = """
    """

    model = Monster
    #form_class = MonsterCreateForm
    template_name = 'agony_monster_detail.html'


class CreateOriginOfAgony(CreateView):
    message = """Life is suffering, sooner or later everyone faces some kind of tragedy, so why not, 
    tell us what happened in your hero past so he felt call for adventure!"""

    model = Origin
    fields = "__all__"
    template_name = 'agony_form.html'
    success_url = reverse_lazy('AGONy_index')


class OriginsOfAgonyList(ListView):
    message = "So many people, so many tragedies, so many heroes!"

    model = Origin
    template_name = 'agony_origin_list.html'


class CreateCommentView(CreateView):
    message = """
    """

    model = Comment
    fields = "__all__"
    template_name = 'agony_form.html'
    success_url = reverse_lazy('AGONy_index')


class CommentListView(ListView):
    message = """
    """

    model = Comment
    template_name = 'agony_comment_list.html'

"""     #hmm, not 
class UpdateOriginOfAgony(LoginRequiredMixin, UpdateView):
    message = ""

    model = Origin
    form_class = OriginCreateForm
    template_name = 'agony_form.html'
    success_url = reverse_lazy('AGONy_monster_list')
"""

class CreateEventInAgony(LoginRequiredMixin, CreateView):
    message = """
    """

    model = Event
    fields = "__all__"
    template_name = 'agony_form.html'
    success_url = reverse_lazy('AGONy_index')


class EventsInAgonyList(LoginRequiredMixin, ListView):
    message = """
    """

    model = Event
    template_name = 'agony_event_list.html'


class UpdateEventInAgony(LoginRequiredMixin, UpdateView):
    message = """
    """

    model = Event
    form_class = EventCreateForm
    template_name = 'agony_form.html'
    success_url = reverse_lazy('AGONy_event_list')

class DetailEventInAgony(LoginRequiredMixin, DetailView):
    message = """
    """

    model = Event
    #form_class = MonsterCreateForm
    template_name = 'agony_event_detail.html'

    
class LeaveAComment(LoginRequiredMixin, CreateView):
    message = """Please, do leave a comment what did you like, did not like or whatever. Much apprecieated anyways!
    """

    model = Comment
    fields = "__all__"
    template_name = 'agony_form.html'
    success_url = reverse_lazy('AGONy_index')


class CommentList(LoginRequiredMixin, ListView):
    message = """List of the comments
    """

    model = Comment
    template_name = 'agony_event_list.html'       


class CreateUserView(View):

    def get(self, request):

        message = """
            Create User - then you can play, maybe even leave a comment what to improve in my game? Be sure to subscribe!
            """

        form = CreateUserForm()
        return render(request, 'agony_form.html', {'form': form, 'message' : message})

    def post(self, request):

        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save(
                commit=False)

            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()

            message = """
                        User created, now go and have some fun!
                        """

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


class CreateMonstersImage(LoginRequiredMixin, CreateView):
    message = """
    """

    model = MonsterImage
    fields = "__all__"
    template_name = 'agony_form.html'
    success_url = reverse_lazy('AGONy_index')


class MonsterImageList(LoginRequiredMixin, ListView):
    message = """
    List of bold, ambitious Heroes awaiting for your command to march into oblivion! Yyy. yes, yes, glory and power, yes.
    """

    model = MonsterImage
    template_name = 'agony_monster_images.html'
