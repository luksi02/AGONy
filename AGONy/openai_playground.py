import openai

def agony3(input_text):
    for i in range(1, 21):

        openai.api_key = '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'  # os.getenv("OPENAI_API_KEY")

        query_response = openai.Completion.create(engine="davinci-instruct-beta", prompt=input_text, temperature=0.8,
                                              max_tokens=200, top_p=1, frequency_penalty=0, presence_penalty=0)

        print("incoming, ", i)

        print(query_response.choices[0].text.split('.'))

        print(i, "completed")

        input_text = "Origin story of a dwarf that lived under dungeon stronhold in shadowy Blue Mountains"

        answer = query_response.choices[0].text.split('.')


prompt = """write a horror-fantasy tale with plot twist about brave hero: Honestly, I knew that I would have to do some work someday to earn my fame, but I never
 imagined how hard it would be', ' Today I met my first Monster', ' But not just any monster: 
 it was an evil"""

agony3(prompt)

