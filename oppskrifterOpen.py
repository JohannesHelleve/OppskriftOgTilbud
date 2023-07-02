import openai
import os
from dotenv import load_dotenv
from OppskriftOgTilbud import push_to_mongo

load_dotenv()

OpenAiAPI = os.getenv('OpenAI')

openai.api_key = OpenAiAPI

def make_recipe():
  oppskrift = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"system", "content": "Lag en oppskrift , formater oppskriften som markdown,\ngjør alle ingrediensene om til en link hvor linken har følgende format, bytt ut SØKEORD\nmed ett naturlig søkeord for ingrediensen [https://kassal.app/varer?sok=[SØKEORD]](https://kassal.app/varer?sok=%5BS%C3%98KEORD%5D)\n\nInkluder navnet på matretten, en beskrivelse på ca 200 ord i begynnelsen av oppskriften og en liste over alle ingrediensene.\n\nEksempel på ingredientsliste format\n\n- 2 fedd [hvitløk](https://kassal.app/varer?sok=hvitl%C3%B8k)\n- Salt og pepper\n- 1 ts [paprikapulver](https://kassal.app/varer?sok=paprikapulver)\n- 1 ts [tørket oregano](https://kassal.app/varer?sok=oregano)"}],
    temperature=1,
    max_tokens=1505,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  jsonOppskrift = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"system", "content": f"Extract the following information:\n- title\n- description\n- ingredients (array with keys amount, unit, text, keyword, include all of them, let the value be null if it can't be extracted),\n- steps (array of strings)\n\nRECEIPE\n\n{oppskrift}\n\nOutput in JSON:"}],
    temperature=1,
    max_tokens=1505,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  return jsonOppskrift

#kan brukes for å finne ut vekt av en del av ingrediensen, men og hente ut vekt fra title til ingrediensen. 
def get_weight_ingrdient(ingredient):
  vekt = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"system", "content": f"Hvor mange gram veier en {ingredient}?"}],
    temperature=1,
    max_tokens=200,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  dict = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"system", "content": f"Fra følgende tekst hent navn på ingrediensen og vekt i gram, og lagre svarene i json format. La vekten være Null hvis den ikke kan bli hentet. {vekt}"}],
    temperature=1,
    max_tokens=200,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  return dict

print(get_weight_ingrdient('Pasta 500g'))