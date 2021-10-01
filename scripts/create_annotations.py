"""
Script to create an annotation file annotations.csv in the format img_name,pokemon_id.
Prints the number of images per pokemon class to provide an overview of the dataset distribution.
"""

import os
import json
import requests

# uncomment to reproduce pokemon_map
# pokeapi_base_url = 'https://pokeapi.co/api/v2/pokemon'
# pokemon_map = {}
# for i in range(1, 152):
#     pokemon = requests.get(f'{pokeapi_base_url}/{i}').json()
#     pokemon_map[pokemon['name']] = i

pokemon_map = {
    "bulbasaur": 1,
    "ivysaur": 2,
    "venusaur": 3,
    "charmander": 4,
    "charmeleon": 5,
    "charizard": 6,
    "squirtle": 7,
    "wartortle": 8,
    "blastoise": 9,
    "caterpie": 10,
    "metapod": 11,
    "butterfree": 12,
    "weedle": 13,
    "kakuna": 14,
    "beedrill": 15,
    "pidgey": 16,
    "pidgeotto": 17,
    "pidgeot": 18,
    "rattata": 19,
    "raticate": 20,
    "spearow": 21,
    "fearow": 22,
    "ekans": 23,
    "arbok": 24,
    "pikachu": 25,
    "raichu": 26,
    "sandshrew": 27,
    "sandslash": 28,
    "nidoran-f": 29,
    "nidorina": 30,
    "nidoqueen": 31,
    "nidoran-m": 32,
    "nidorino": 33,
    "nidoking": 34,
    "clefairy": 35,
    "clefable": 36,
    "vulpix": 37,
    "ninetales": 38,
    "jigglypuff": 39,
    "wigglytuff": 40,
    "zubat": 41,
    "golbat": 42,
    "oddish": 43,
    "gloom": 44,
    "vileplume": 45,
    "paras": 46,
    "parasect": 47,
    "venonat": 48,
    "venomoth": 49,
    "diglett": 50,
    "dugtrio": 51,
    "meowth": 52,
    "persian": 53,
    "psyduck": 54,
    "golduck": 55,
    "mankey": 56,
    "primeape": 57,
    "growlithe": 58,
    "arcanine": 59,
    "poliwag": 60,
    "poliwhirl": 61,
    "poliwrath": 62,
    "abra": 63,
    "kadabra": 64,
    "alakazam": 65,
    "machop": 66,
    "machoke": 67,
    "machamp": 68,
    "bellsprout": 69,
    "weepinbell": 70,
    "victreebel": 71,
    "tentacool": 72,
    "tentacruel": 73,
    "geodude": 74,
    "graveler": 75,
    "golem": 76,
    "ponyta": 77,
    "rapidash": 78,
    "slowpoke": 79,
    "slowbro": 80,
    "magnemite": 81,
    "magneton": 82,
    "farfetchd": 83,
    "doduo": 84,
    "dodrio": 85,
    "seel": 86,
    "dewgong": 87,
    "grimer": 88,
    "muk": 89,
    "shellder": 90,
    "cloyster": 91,
    "gastly": 92,
    "haunter": 93,
    "gengar": 94,
    "onix": 95,
    "drowzee": 96,
    "hypno": 97,
    "krabby": 98,
    "kingler": 99,
    "voltorb": 100,
    "electrode": 101,
    "exeggcute": 102,
    "exeggutor": 103,
    "cubone": 104,
    "marowak": 105,
    "hitmonlee": 106,
    "hitmonchan": 107,
    "lickitung": 108,
    "koffing": 109,
    "weezing": 110,
    "rhyhorn": 111,
    "rhydon": 112,
    "chansey": 113,
    "tangela": 114,
    "kangaskhan": 115,
    "horsea": 116,
    "seadra": 117,
    "goldeen": 118,
    "seaking": 119,
    "staryu": 120,
    "starmie": 121,
    "mr-mime": 122,
    "scyther": 123,
    "jynx": 124,
    "electabuzz": 125,
    "magmar": 126,
    "pinsir": 127,
    "tauros": 128,
    "magikarp": 129,
    "gyarados": 130,
    "lapras": 131,
    "ditto": 132,
    "eevee": 133,
    "vaporeon": 134,
    "jolteon": 135,
    "flareon": 136,
    "porygon": 137,
    "omanyte": 138,
    "omastar": 139,
    "kabuto": 140,
    "kabutops": 141,
    "aerodactyl": 142,
    "snorlax": 143,
    "articuno": 144,
    "zapdos": 145,
    "moltres": 146,
    "dratini": 147,
    "dragonair": 148,
    "dragonite": 149,
    "mewtwo": 150,
    "mew": 151
}

annotation_str = 'img_path,pokemon_id\n'
name_count = {}

os.chdir('./data/images')
for file in os.listdir():       # e.g. pikachu012.jpg
    name = file.split('.')[0]   # removes .jpg
    name = name[:-3]            # removes 012
    
    annotation_str += f'{file},{pokemon_map[name]}\n'

    if name not in name_count:
        name_count[name] = 1
    else:
        name_count[name] += 1

os.chdir('..')
with open('annotations.csv', 'w') as f:
    f.write(annotation_str)
os.chdir('..')

print('Annotations created.')
print('Images per pokemon. Consider manually adding images to rare pokemon classes.')
print(json.dumps(dict(sorted(name_count.items(), key=lambda item: item[1])), indent=4))
