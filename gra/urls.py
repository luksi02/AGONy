"""gra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

from AGONy.views import (AGONyIndexView, AGONyWorkInProgress, CreateHeroInAgony,
                         CreateMonsterInAgony, Leaderboard, UpdateHeroInAgony, MonstersInAgonyList,
                         UpdateMonsterInAgony, CreateDefaultsInAgony,
                         CreateUserView, LoginView, LogoutView, MyHeroesInAgonyList, CreateEventInAgony,
                         EventsInAgonyList, UpdateEventInAgony, ContactView, CreateCommentView, CommentListView,
                         CreateOriginOfAgony, OriginsOfAgonyList, CreateMonstersImage, MonsterImageList
                         )

from AGONy.views_mechanicus import (StageDetailView, agony,
                                    AttackMonsterView, CreateJourneyForHero, JourneyDetailView, agony2, FoundSomething,
                                    OhCrapItsATrap, RunAway, ReturnToJourney, CreateGameForHero)

urlpatterns = [

    #agony start, login not required

    path('', AGONyIndexView.as_view(), name='AGONy_index'),
    path('wip/', AGONyWorkInProgress.as_view(), name='AGONy_WIP'),
    path('AGONy_all_heroes/', Leaderboard.as_view(), name='AGONy_hero_list'), #Leaderboard
    path('AGONy_contact/', ContactView.as_view(), name='AGONy_contact'), #Contact

    path('AGONy_create_comment/', CreateCommentView.as_view(), name='AGONy_create_comment'), #Comment
    path('AGONy_all_comments/', CommentListView.as_view(), name='AGONy_comment_list'), #Comment

    # complaints_for_superuser

    #path('AGONy_contact/', HeroesInAgonyList.as_view(), name='AGONy_contact'), #Leaderboard

    #agony CRUD
    path('AGONy_create_defaults/', CreateDefaultsInAgony.as_view(), name='AGONy_create_defaults'),
    path('AGONY_create_hero/', CreateHeroInAgony.as_view(), name='AGONy_create_hero'),
    path('AGONY_create_monster/', CreateMonsterInAgony.as_view(), name='AGONy_create_monster'),
    path('AGONy_create_user/', CreateUserView.as_view(), name='AGONy_create_user'),
    path('AGONy_create_event/', CreateEventInAgony.as_view(), name='AGONy_create_event'),
    path('AGONy_create_origin/', CreateOriginOfAgony.as_view(), name='AGONy_create_origin'),
    path('AGONy_create_monsters_image/', CreateMonstersImage.as_view(), name='AGONy_create_monsters_image'),

    path('AGONy_my_heroes/', MyHeroesInAgonyList.as_view(), name='AGONy_my_hero_list'),
    path('AGONy_all_monsters/', MonstersInAgonyList.as_view(), name='AGONy_monster_list'),
    path('AGONy_all_events/', EventsInAgonyList.as_view(), name='AGONy_event_list'),
    path('AGONy_all_origins/', OriginsOfAgonyList.as_view(), name='AGONy_origin_list'),
    path('AGONy_monster_image_list/', MonsterImageList.as_view(), name='AGONy_monster_image_list'),

    path('AGONy_update_monster/<int:pk>', UpdateMonsterInAgony.as_view(), name='AGONy_update_monster'),
    path('AGONy_update_hero/<int:pk>', UpdateHeroInAgony.as_view(), name='AGONy_update_hero'),
    path('AGONy_update_event/<int:pk>', UpdateEventInAgony.as_view(), name='AGONy_update_event'),

    #AGONy_mechanicus
    #fight_creation
    path('AGONy_create_game/<int:id_hero>/', CreateGameForHero.as_view(), name='AGONy_create_game_for_hero'),
    path('AGONy_stage_detail/<int:pk>/', StageDetailView.as_view(), name='AGONy_stage_detail'),

    #fight_action
    path('AGONy_attack_monster/<int:monster_id>/<int:hero_id>/', AttackMonsterView.as_view(), name='AGONy_attack_monster'),

    #journey_creation
    path('AGONy_create_journey/<int:id_hero>/', CreateJourneyForHero.as_view(), name='AGONy_create_journey_for_hero'),
    path('AGONy_journey_detail/<int:pk>/', JourneyDetailView.as_view(), name='AGONy_journey_detail'),

    #journey_actions
    path('AGONy_found_something/<int:pk>/', FoundSomething.as_view(), name='AGONy_found_something'),
    path('AGONy_trap/<int:pk>/', OhCrapItsATrap.as_view(), name='AGONy_trap'),
    path('AGONy_run_away/<int:pk>/', RunAway.as_view(), name='AGONy_run_away'),
    path('AGONy_return_to_journey/<int:pk>/', ReturnToJourney.as_view(), name='AGONy_return_to_journey'),

    #WIP
    #path('fight/<int:stage_id>/', rpg.views.FightView.as_view(), name='fight'),
    # not-so-needed
    #path('detail_game/<int:pk>/', rpg.views.GameDetailView.as_view(), name='game_detail'),
    #path('create_game/', rpg.views.CreateGameView.as_view(), name='create_game'),

    # AI
    path('agony_AI/', agony, name='agony_AI'),
    path('agony_AI_2/', agony2, name='agony_AI_2'),

    # AGONy login/auth
    path('AGONy_login/', LoginView.as_view(), name='AGONy_login'),
    path('AGONy_logout/', LogoutView.as_view(), name='AGONy_logout'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

"""if settings.DEBUG:
    urlpatterns += [
        path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]"""
