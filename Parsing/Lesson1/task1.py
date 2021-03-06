import requests
import json

header = {
    'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
url = 'https://api.github.com/users/octocat/repos'

repos = []
response = requests.get(url, headers=header).json()
for i in range(1, len(response)):
        obj = response[i]
        repos.append(obj.get('name'))

f = open('result_task1.json', 'w')
to_json = json.dumps(repos)
json.dump(to_json, f)
f.close()