import requests
import json


def get_superhero():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    resp = requests.get(url)
    if resp.status_code == 200:
        resp = resp.text
        resp = json.loads(resp)
        return resp
    else:
        message = '! - Error / Ошибка'
        return message


def best_superhero():
    heroes = {}
    for item in superheroes:
        name = item['name']
        if name in list_name:
            key = name
            list_powerstats = item['powerstats']
            value = list_powerstats['intelligence']
            heroes[key] = value
            max_intelligence = max(heroes.values())
            max_key = max(heroes, key=heroes.get)
    return f'Самый умный супергерой {max_key} с уровнем интеллекта {max_intelligence}'

    if len(heroes) == 0:
        return f'По данным {list_name} и {powerstats} ничего не найдено.'


superheroes = get_superhero()
list_name = ['Hulk', 'Captain America', 'Thanos']
powerstats = 'intellience'

print(best_superhero())
