import json

cities = []
cities_with_names = []
data = None
airports = None
with open('data.json') as f:
    data = json.load(f)

with open('airport_data.json') as f:
    airports = json.load(f)

with open('colors.json') as f:
    colors = json.load(f)

for city in data:
    cities.append(city['host'])

unique = set(cities)

for city in unique:
    cities_with_names.append({"code": city.upper(), "city_name": airports[city.upper()], "color": colors[city]})

# {'ams', 'tpe', 'sin', 'syd', 'den', 'atl', 'sea', 'dca', 'mxp', 'sjc', 
# 'mia', 'ewr', 'gru', 'bur', 'vie', 'cdg', 'dfw', 'bom', 'hkg', 'arn', 
# 'lhr', 'fra', 'jnb', 'ord', 'yyz', 'nrt', 'mad', 'kix'}

with open('BONUS_data.json', 'w') as writeJSON:
   json.dump(cities_with_names, writeJSON, ensure_ascii=False)