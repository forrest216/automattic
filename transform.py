import json

with open('airports.json') as f:
    airports = json.load(f)

revised = {}

for airport in airports:
   revised[airport["code"]] = airport["city"]


with open('airport_data.json', 'w') as writeJSON:
   json.dump(revised, writeJSON, ensure_ascii=False)
