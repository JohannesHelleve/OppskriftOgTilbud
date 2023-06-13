import openai
import config
from OppskriftOgTilbud import push_grocery_to_mongo

openai.api_key = config.OpenAI

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

push_grocery_to_mongo(jsonOppskrift)
