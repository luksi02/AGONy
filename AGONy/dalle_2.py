import openai
import urllib.request
from datetime import datetime

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



