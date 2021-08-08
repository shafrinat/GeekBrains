import requests
import json

header = {
    'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
# Last.fm api
url = 'http://ws.audioscrobbler.com/2.0/'

# Используется авторизация по api_key
params = {
    'api_key': '5481c963f854eacc2b8b32128ebe3aaa',
    'method': 'chart.getTopTracks',
    'format': 'json'
}

response = requests.get(url, headers=header, params=params).json()

f = open('result_task2.json', 'w')
to_json = json.dumps(response)
json.dump(to_json, f)
f.close()

# Код ниже для получения информации из ответа api
# a = response.get('tracks')
# b = a.get('track')
# for i in range(0, len(b)):
#     c = b[i]
#     name = c.get('name')
#     d = c.get('artist')
#     artist = d.get('name')
#     print(f'Номер {i+1}: {artist} с треком "{name}"')