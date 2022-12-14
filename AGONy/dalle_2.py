import openai
import urllib.request
from datetime import datetime

def dalle2(prompt):
    openai.api_key = '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'
    response = openai.Image.create(

        prompt="black & white heroic style image of :barbarian glancing at the skull of fallen foe, with a litte smug on his victoriues face",
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
    date_string = now.strftime("%Y_%m_%Y_%H_%M_%S")

    print(date_string)
    dalle_output_dir = "/home/luksi02/DALL_E/2022_12_13/"+date_string+".png"
    print(dalle_output_dir)
    urllib.request.urlretrieve(image_url, dalle_output_dir)
    return print("alles_gut!")

def dalle2_in_loop(n):
    for i in range(1, n+1):
        print(i)
        prompt = "black & white fnatasy heroic style image of :barbarian glancing at the skull of fallen foe, with a litte smug on his victoriues face"
        dalle2(prompt)
        print(i, "complete")

prompt = "black & white heroic style image of :barbarian glancing at the skull of fallen foe, with a litte smug on his victoriues face"

#dalle2(prompt)
dalle2_in_loop(5)


