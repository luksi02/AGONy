import openai
import urllib.request
from datetime import datetime
from openai_apikey import OPENAI_API_KEY

def dalle2(prompt):
    openai.api_key = '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'
    response = openai.Image.create(

        prompt=prompt,
        #"black & white heroic style image of :barbarian glancing at the skull of fallen foe, with a litte smug on his victoriues face",
        #"black & white heroic style image of :white siamese cat holding a sword that is actually a possessed by demon and wants to devour some souls, now it looks for some snack",
        n=1,
        size="1024x1024"

    )
    # print(image_url=response['data'][0]['url'])
    image_url=response['data'][0]['url']
    print(image_url)
    #urllib.request.urlretrieve(image_url, "/home/luksi02/DALL_E/2022_12_13/3.png")
    now = datetime.now()
    print(now)
    date_string = now.strftime("%Y_%m_%d_%H_%M_%S")

    print(date_string)
    dalle_output_dir = "/home/luksi02/DALL_E/spirit"+date_string+".png"
    print(dalle_output_dir)
    urllib.request.urlretrieve(image_url, dalle_output_dir)
    return print("alles_gut!")

def dalle2_in_loop(n):
    for i in range(1, n+1):
        print(i)
        #prompt = "fantasy heroic comic-style image of :barbarian glancing at the skull of fallen foe, with a litte smug on his victoriues face"
        dalle2(prompt)
        print(i, "complete")

barbarian_prompt = "fantasy heroic comic-style image of :barbarian glancing at the skull of fallen foe at his hands, with a litte smug on his victorious face"

AGONy_monster_goblin = "fantasy heroic comic-style image of Goblin :Little, nasty green creature, filled with hate and hunger - looks like it wants to be its next meal!"
AGONy_monster_orc = """horror-fantasy heroic comic-style image of Orc :Big, angry green creature that finds you very attractive... as a food, 
                               and you guessed it - it means you should be afraid!"""

AGONy_monster_bandit="""horror-fantasy heroic comic-style image of Bandit :ever heard saying: dont talk to strangers? Well, one od them just approached you, and seems like he 
                               wants to befriend you - why elese would he shout "Your money or your life!"?"""


AGONy_monster_wolf="""horror-fantasy heroic comic-style image of Wolf :Ever heard tales and stories why you 
                                should not walk into the woods? You guessed it - here comes 
                                the wolf and it counts you'll be a fancy snack!"""

AGONy_monster_spider="""horror-fantasy heroic comic-style image of Spider: Itsy bitsy giant venomous spider - Oh, I'm so cute:
                                I have eight long furry legs, eight terryfing eyes set on you, and you 
                                guessed it! I want some cuddels and cover you in webs and then eat! Come to papa!"""

AGONy_monster_angry_bird_bear = """horror-fantasy heroic comic-style image of Angry Bird-Bear: Have you ever heard of angry bird? Probably. 
                               Heard of angry bear? Probably. Heard of Bird-Bear? Never? Well, some kind of 
                               psycho-druid created this abonomination, and now it's up to you to face IT. 
                               And get rid of IT. For everyone!"""

AGONy_monster_dragon = """horror-fantasy heroic comic-style image of Angry Dragon: Mystic and poud creature, but (there's always a but!) has a 
                               nasty habit - it hoards anything gold-like and shiny! (it wants a new addition 
                               to it's collection, and you guessed it - it wants you and your shines!"""

AGONy_monster_zombie = """horror-fantasy heroic comic-style image of Angry Zombie"""

"""Clumsy, stinking, brainless... 
                                those damn zombies! Ugh, one 
                               just dropped its liver. DISGUSTANG! Well, brainless for now - it wants your 
                               brainzzz! Now protect it or 
                               become another brainless, wiggly, rotting walking zombie!"""


AGONy_monster_skeleton = """horror-fantasy heroic comic-style image of Angry Skeleton: There's something there! Something white and full of calcium. 
                               Hey, why those bones hover in air? 
                               Hey, why those skull turned into my direction? Oh hell no, why it moves 
                               towards me? Shouldn't it behave nicely and just stay dead?"""

AGONy_monster_spirit = """horror-fantasy heroic comic-style image of Angry-Vegenful Spirit: some spirits stay on earth even after death - mostly 
                               because their life was ended tragically. 
                               Now you encountered one. Not a pleasant spirit this one is, oh no."""

#by murder or other foul action.

AGONy_monster_ = """horror-fantasy heroic comic-style image of Angry """

prompt = AGONy_monster_spirit


#dalle2(prompt)
dalle2_in_loop(10)


"""
Andrew, One-eyed war-experienced Octopus - an octopi war veteran, tired of life, combatant and commander in Sixth Deep Sea war, now retired, and what now? You just came to spoil his rest, get to arms! Prepare for squishy hugs and chokes!

Trinity, the demon-pig. You know pigs, dont you? Funny animals full of delicious bacon. Not this one. This one is full of hate and considers you its delicious bacon. Run or prepare to be eaten alive!

Beholder - I spy with my little eye, actually with my every eye, and my spying tells me you are quite a snack, come closer so I can take a little bite, you look like a tasty tasty snack! So tasty!

Jack, the Yellow-Magnetic-Star - in the beginning there was not much, but Jack was already theere. Immortal, just like alkohol. Cuts swiftly through air like a leszczyna, seems like you are his next target. Remember, you the motyka, Jack - the sun.

Bitsy the Courageous - Volcanic Ladybug - ahh, ladybugs, such a peaceful, adorable creatures! Well, not this one - this one spits fiare and lava, and wants you to be it's next takeaway food! Yikes!

Fnacy Rainbow-Colored Unicorn - A unicorn! What a wonderful walking real wonder! Wait, why does it chew a human body? Wait, why does it suddenly look interested in me? Wait, what? Why it runs towards me licking its tounge? Somebody please help me from this wonder! HELP! HELP!
"""


"""
Your Hero encountered Monster, now stand and fight it! 
                             Or try to run, just to live another day! No judgement here, world is hard enough even without fighting monsters!
['\n\nMy dearest diary! It is 11th day of my quest to earn fame and glory! New day comes', ' New challenges', " Hope I, the Percy McPerson, am ready for what comes next and I'm ready for these adventures! Maybe one day I will be remembered as a legend? Let's find out! Meanwhile, today's adventure: Your Hero encountered Monster, now stand and fight it!\n                                            Or try to run, just to live another day! No judgement here, world is hard enough even without fighting monsters!"]
[09/Jan/2023 21:07:59] "GET /AGONy_journey_detail/17/ HTTP/1.1" 200 3747
[09/Jan/2023 21:08:06] "GET /AGONy_create_game/1/ HTTP/1.1" 302 0
Goblin
[09/Jan/2023 21:08:06] "GET /AGONy_stage_detail/4/ HTTP/1.1" 200 3061
/home/luksi02/AGONy/AGONy/models.py changed, reloading.
^CTraceback (most recent call last):
  File "manage.py", line 22, in <module>
    main()
  File "manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "/home/luksi02/AGONy/venv/lib/python3.8/site-packages/django/core/management/__init__.py", line 446, in execute_from_command_line
    utility.execute()
  File "/home/luksi02/AGONy/venv/lib/python3.8/site-packages/django/core/management/__init__.py", line 398, in execute
    autoreload.check_errors(django.setup)()
  File "/home/luksi02/AGONy/venv/lib/python3.8/site-packages/django/utils/autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "/home/luksi02/AGONy/venv/lib/python3.8/site-packages/django/__init__.py", line 17, in setup
    from django.utils.log import configure_logging
  File "/home/luksi02/AGONy/venv/lib/python3.8/site-packages/django/utils/log.py", line 6, in <module>
    from django.core import mail
  File "/home/luksi02/AGONy/venv/lib/python3.8/site-packages/django/core/mail/__init__.py", line 10, in <module>
    from django.core.mail.message import (
  File "/home/luksi02/AGONy/venv/lib/python3.8/site-packages/django/core/mail/message.py", line 4, in <module>
    from email import generator, message_from_string
  File "/usr/lib/python3.8/email/generator.py", line 21, in <module>
    NLCRE = re.compile(r'\r\n|\r|\n')
  File "/usr/lib/python3.8/re.py", line 250, in compile
    def compile(pattern, flags=0):
KeyboardInterrupt
(venv) luksi02@luksi02-VirtualBox:~/AGONy$ python3 manage.py makemigrations
Migrations for 'AGONy':
  AGONy/migrations/0006_alter_monster_monsters_gold.py
    - Alter field monsters_gold on monster
(venv) luksi02@luksi02-VirtualBox:~/AGONy$ python3 manage.py migrate
Operations to perform:
  Apply all migrations: AGONy, admin, auth, contenttypes, sessions
Running migrations:
  Applying AGONy.0006_alter_monster_monsters_gold...Traceback (most recent call last):
  File "manage.py", line 22, in <module>
    main()
  File "manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "/home/luksi02/AGONy/venv/lib/python3.8/site-packages/django/core/management/__init__.py", line 446, in execute_from_command_line
    utility.execute()
  File "/home/luksi02/AGONy/venv/lib/python3.8/site-packages/django/core/management/__init__.py", line 440, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/home/luksi02/AGONy/venv/lib/python3.8/site-packages/django/core/management/base.py", line 402, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/home/luksi02/AGONy/venv/lib/python3.8/site-packages/django/core/management/base.py", line 448, in execute
    output = self.handle(*args, **options)
  File "/home/luksi02/AGONy/venv/lib/python3.8/site-packages/django/core/management/base.py", line 96, in wrapped
    res = handle_func(*args, **kwargs)
  File "/home/luksi02/AGONy/venv/lib/python3.8/site-packages/django/core/management/commands/migrate.py", line 349, in handle
    post_migrate_state = executor.migrate(
  File "/home/luksi02/AGONy/venv/lib/python3.8/site-packages/django/db/migrations/executor.py", line 135, in migrate
    state = self._migrate_all_forwards(
  File "/home/luksi02/AGONy/venv/lib/python3.8/site-packages/django/db/migrations/executor.py", line 167, in _migrate_all_forwards
    state = self.apply_migration(
  File "/home/luksi02/AGONy/venv/lib/python3.8/site-packages/django/db/migrations/executor.py", line 255, in apply_migration
    migration_recorded = True
  File "/home/luksi02/AGONy/venv/lib/python3.8/site-packages/django/db/backends/sqlite3/schema.py", line 39, in __exit__
    self.connection.check_constraints()
  File "/home/luksi02/AGONy/venv/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py", line 264, in check_constraints
    raise IntegrityError(
django.db.utils.IntegrityError: The row in table 'AGONy_monstermonsterimage' with primary key '4' has an invalid foreign key: AGONy_monstermonsterimage.monster_image_id contains a value '4' that does not have a corresponding value in AGONy_monsterimage.id.
(venv) luksi02@luksi02-VirtualBox:~/AGONy$ python3 manage.py migrate
Operations to perform:
  Apply all migrations: AGONy, admin, auth, contenttypes, sessions
Running migrations:
  Applying AGONy.0006_alter_monster_monsters_gold... OK
(venv) luksi02@luksi02-VirtualBox:~/AGONy$ python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 09, 2023 - 21:11:18
Django version 4.1.3, using settings 'gra.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Goblin
[09/Jan/2023 21:11:22] "GET /AGONy_stage_detail/4/ HTTP/1.1" 200 3061
[09/Jan/2023 21:11:32] "GET /AGONy_attack_monster/4/1/ HTTP/1.1" 302 0
Goblin
[09/Jan/2023 21:11:32] "GET /AGONy_stage_detail/4/ HTTP/1.1" 200 3061
[09/Jan/2023 21:11:33] "GET /AGONy_attack_monster/4/1/ HTTP/1.1" 302 0
Goblin
[09/Jan/2023 21:11:33] "GET /AGONy_stage_detail/4/ HTTP/1.1" 200 3060
[09/Jan/2023 21:11:33] "GET /AGONy_attack_monster/4/1/ HTTP/1.1" 302 0
Goblin
[09/Jan/2023 21:11:34] "GET /AGONy_stage_detail/4/ HTTP/1.1" 200 3072
[09/Jan/2023 21:11:35] "GET /AGONy_return_to_journey/1/ HTTP/1.1" 302 0
watch your step! While watching beautiful bird you fell into a cave, a dark, dark cave. 
        Youre lucky you didnt break your legs. Anyway, escaping cave took a lot od time.
[' One day, a lot of time', ' It was a lot of time', '\n              Finally, you found a way out! You found a beautiful bird on the way and it was singing', ' You followed the bird, but sadly, it was just an ordinary bird', '\n                      The End!\n\nMy dearest diary! It is 12th day of my quest to earn fame and glory! New day comes', ' New challenges', " Hope I, the Percy McPerson, am ready for what comes next and I'm ready for these adventures! Maybe one day I will be remembered as a legend? Let's find out!\n              Meanwhile, today's adventure: watch your step! While watching beautiful bird you fell into a cave, a dark, dark cave", " You're lucky you"]
[09/Jan/2023 21:11:43] "GET /AGONy_journey_detail/18/ HTTP/1.1" 200 3841
[09/Jan/2023 21:11:46] "GET /AGONy_trap/19/ HTTP/1.1" 302 0
While  wandering through plains you felt watched - 
        but it's too late to do anything else but fight! Draw your weapon!
['    \n\nMy dearest diary! It is 13th day of my quest to earn fame and glory! New day comes', ' New challenges', " Hope I, the Percy McPerson, am ready for what comes next and I'm ready for these adventures! Maybe one day I will be remembered as a legend? Let's find out!\n Meanwhile, today's adventure:\n     While  wandering through plains you felt watched \n                                                                                                            "]
[09/Jan/2023 21:11:53] "GET /AGONy_journey_detail/19/ HTTP/1.1" 200 3409
[09/Jan/2023 21:12:02] "GET /AGONy_my_heroes/ HTTP/1.1" 200 3680
[09/Jan/2023 21:12:04] "GET /AGONy_create_journey/1/ HTTP/1.1" 302 0
[09/Jan/2023 21:12:04] "GET /AGONy_return_to_journey/1/ HTTP/1.1" 302 0
Ooh, shiney! You found something! Seems like after all it was worth to walk 
                            and put yourself in all this danger. Now let's see what you found!
["\n\nToday's adventure:\n\nOoh, shiney! You found something! Seems like after all it was worth to walk so much and put yourself in all this danger", " Now let's see what you found!\n\nIt's a \n\nPiece of a cooking pan!\n\nGreat! Now I can make more rice!\n\nHuh? You want to know what I'm talking about? I'm talking about rice!\n\nYes, rice", ' A popular food', " \n\nIt's a\n\nPiece of a cooking pan!\n\nGreat! Now I can make more rice!\n\nHuh? You want to know what I'm talking about? I'm talking about rice!\n\nYes, rice", ' A popular food', "\n\nI don't know what this means", '']
[09/Jan/2023 21:12:10] "GET /AGONy_journey_detail/20/ HTTP/1.1" 200 3756
[09/Jan/2023 21:12:12] "GET /AGONy_found_something/21/ HTTP/1.1" 302 0
wandering through Forest you notice more and more dead trees. Then, you 
        notice why - you stumble upon an old and grim crypt - do you dare to enter IT?
['\n\nMy dear diary-\n\nToday was a good day', ' I was out on my quest and I managed to kill two monsters', ' One tried to kill me with a spear, so I responded in kind by stabbing it on the head', ' The other one tried to attack me with a club, but I cut it in half with my sword', " It was great! But then I stumbled upon a crypt, and I'm not sure what to do", ' I was about to enter, but I decided to stop', " I'm not sure if I want to enter", " What if the monsters inside are stronger than the ones I killed today? What if the monsters are hiding a treasure? I'm not sure", ' The only thing I know is that this crypt is an obstacle on my way to fame', '\n\nI have to keep going', '\n\nPercy McPerson\n\nI found a dead tree!']
[09/Jan/2023 21:12:18] "GET /AGONy_journey_detail/21/ HTTP/1.1" 200 3774
/home/luksi02/AGONy/AGONy/views_mechanicus.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 09, 2023 - 21:13:17
Django version 4.1.3, using settings 'gra.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

"""