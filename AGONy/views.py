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
    template_name = 'agony_form.html'


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
    

class CreateDefaultsInAgony(View):

    def get(self, request):

        """message =
            Let's just create some defaults for you to play already, who wants to go through boring creating the world?
            """

        # A view to create some defaults in game!
        Hero.objects.create(name='Percy McPerson', race=0)
        Hero.objects.create(name='Woody Oakson', race=1)
        Hero.objects.create(name='Shorty MacBeard', race=2)

        # human-like monsters, but not exactly - orcs and stuff
        Monster.objects.create(name='Goblin', hp=20, attack=2, defence=0, monster_level=0, monster_type=0, 
                               description="""Little, nasty green creature, filled with hate and hunger - looks like it wants to be its next meal!""")
        
        Monster.objects.create(name='Orc', hp=40, attack=3, defence=1, monster_level=1, monster_type=0, 
                               description="""Big, angry green creature that finds you very attractive... as a food, 
                               and you guessed it - it means you should be afraid!""")        
             
        #Monster.objects.create(name='Goblin Wolf Rider', hp=50, attack=7, defence=4, monster_level=2, monster_type=0)
        #Monster.objects.create(name='Troll', hp=80, attack=8, defence=2, monster_level=3, monster_type=0)
        #Monster.objects.create(name='Giant', hp=200, attack=15, defence=5, monster_level=4, monster_type=0)
        
        #humans - but nasty ones        
        Monster.objects.create(name='Bandit', hp=40, attack=3, defence=1, monster_level=1, monster_type=0, 
                               description="""ever heard saying: dont talk to strangers? Well, one od them just approached you, and seems like he 
                               wants to befriend you - why elese would he shout "Your money or your life!"?""")

        # wild-wild-life monsters
        Monster.objects.create(name='Wolf', hp=25, attack=3, defence=0, monster_level=0, monster_type=1,
                               description="""Ever heard tales and stories why you 
                                should not walk into the woods? You guessed it - here comes 
                                the wolf and it counts you'll be a fancy snack!""")
        
        Monster.objects.create(name='Giant Venomous Spider', hp=50, attack=3, defence=0, monster_level=1,
                               monster_type=1, description="""Itsy bitsy giant venomous spider - Oh, I'm so cute:
                                I have eight long furry legs, eight terryfing eyes set on you, and you 
                                guessed it! I want some cuddels and cover you in webs and then eat! Come to papa!""")
        
        Monster.objects.create(name='Angry Bird-Bear', hp=80, attack=5, defence=1, monster_level=2, monster_type=1,
                               description="""Have you ever heard of angry bird? Probably. 
                               Heard of angry bear? Probably. Heard of Bird-Bear? Never? Well, some kind of 
                               psycho-druid created this abonomination, and now it's up to you to face IT. 
                               And get rid of IT. For everyone!""")
        
        #Monster.objects.create(name='Fancy Unicorn', hp=100, attack=5, defence=2, monster_level=3, monster_type=1)
        
        Monster.objects.create(name='Dragon', hp=150, attack=10, defence=3, monster_level=4, monster_type=1, 
                               description="""Mystic and poud creature, but (there's always a but!) has a 
                               nasty habit - it hoards anything gold-like and shiny! (it wants a new addition 
                               to it's collection, and you guessed it - it wants you and your shines!""")

        # undead monsters
        Monster.objects.create(name='Zombie', hp=40, attack=2, defence=0, monster_level=0, monster_type=2, 
                               description="""Clumsy, stinking, brainless... those damn zombies! Ugh, one 
                               just dropped its liver. DISGUSTANG! Well, brainless for now - it wants your 
                               brainzzz! Now protect it or 
                               becomen another brainless, wiggly, rotting walking corpse!""")

        Monster.objects.create(name='Skeleton', hp=55, attack=3, defence=0, monster_level=1, monster_type=2, 
                               description="""There's something there! Something white and full of calcium. 
                               Hey, why those bones hover in air? 
                               Hey, why those skull turned into my direction? Oh hell no, why it moves 
                               towards me? Shouldn't it behave nicely and just stay dead?""")
        
        Monster.objects.create(name='Vegenful Spirit', hp=60, attack=6, defence=6, monster_level=2, monster_type=2,
                               description="""some spirits stay on earth even after death - mostly 
                               because their life was ended by murder or other foul action. 
                               Now you encountered one. Not a pleasant spirit this one is, oh no.""")
        
        #Monster.objects.create(name='Lich', hp=80, attack=15, defence=3, monster_level=3, monster_type=2)
        
        #Monster.objects.create(name='Vampire', hp=125, attack=6, defence=5, monster_level=4, monster_type=2)

        # origins - general
        #Origin.objects.create(origin_type=0, origin_description="Tired of mundane life, felt call for adventure")
        #Origin.objects.create(origin_type=0, origin_description="Want to get rich fast, or die trying")
        #Origin.objects.create(origin_type=0, origin_description="Got lured to adventure by songs of riches and glory")
        #Origin.objects.create(origin_type=0, origin_description="Broke the law, it's desperate try to clear name")

        # origins - tragic
        Origin.objects.create(origin_type=0,
                              origin_description="Got his family murdered, now on a quest to avenge them!")
        
        Origin.objects.create(origin_type=0,
                              origin_description="Murdered a lot of people, now running away from law enforcement!")
        
        Origin.objects.create(origin_type=0, origin_description="Got set up in criminal activity, it's a way to repent")

        # default user creation
        #User.objects.create(username='abc', password1='12345678', password2='12345678')
        #User.objects.create(username='xyz', password1='12345678', password2='12345678')

        #0 - escape-able monster encounter
        Event.objects.create(event_type=0, event_name="""Your Hero encountered Monster, now stand and fight it! 
                             Or try to run, just to live another day! No judgement here, world is hard enough even without fighting monsters!""")
        
        #1 - loot encounter
        Event.objects.create(event_type=1, event_name="""Ooh, shiney! You found something! Seems like after all it was worth to walk 
                            and put yourself in all this danger. Now let's see what you found!""")
        
        #2 - trap
        Event.objects.create(event_type=2, event_name="""Oh crap, it's a trap! Of course when did you find it out? Just when you stepped
                            into that trap and sprung it! Damn, it must have hurt! How are you holding up? Still have all limbs?""")
        
        #3 - empty encounter
        Event.objects.create(event_type=3, event_name="""Wonderful views, aren't they? So beautiful landscape! 
                            You take a while to just enjoy this peaceful moment, after all saving the world (or conquering it, or 
                            anything else you doing, can wait a little moment)""")
        
        #2 - Trap
        Event.objects.create(event_type=2, event_name="""watch your step! While watching beautiful bird you fell into a cave, a dark, dark cave. 
        Youre lucky you didnt break your legs. Anyway, escaping cave took a lot od time.""")
        
        #4 - Ambush-fight
        Event.objects.create(event_type=4, event_name="""While  wandering through plains you felt watched - 
        but it's too late to do anything else but fight! Draw your weapon!""")
        
        #5 - Visitable crypt - undead monsters
        Event.objects.create(event_type=5, event_name="""wandering through Forest you notice more and more dead trees. Then, you 
        notice why - you stumble upon an old and grim crypt - do you dare to enter IT?""")        
       
        #6 - Healing encounter
        Event.objects.create(event_type=6, event_name="""Amidst nowhere, you found a beautiful, blossoming oasis. You 
        take a well-deserved sip of crystal-clear water and at instant feel refreshed and more vigorous.""")

        return redirect('AGONy_index')  #, {'message': message})


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
