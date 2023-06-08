import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="I want a Recipe that contains: tomato and onion. The recipe needs a headline, short description, a step by step guide and a list of the items in the recipe. All in norweigan\n",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)