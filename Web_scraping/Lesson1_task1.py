# Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного
# пользователя(input или argparse), сохранить JSON-вывод в файле *.json; написать функцию, возвращающую(return)
# список репозиториев.

import requests
import json

SAVE_REPOS_PATH = "repos.json"


# Создаем url из имени пользователя
def make_url(user_name):
    url = f"https://api.github.com/users/{user_name}/repos"
    return url


# Создаем список репозиториев
def make_repos_list(url):
    repos = []
    response = requests.get(url).json()
    for i in range(len(response)):
        obj = response[i]
        repos.append(obj.get('name'))
    return repos


# Сохраняем список репозиториев в json
def save_repos_list(repos_list, path):
    with open(path, "w") as f:
        json.dump(repos_list, f, indent=2)


# Собираем все в конвейер
def pipeline(path):
    username = input("Username on GitHub: ")
    url = make_url(username)
    repos_list = make_repos_list(url)
    save_repos_list(repos_list, path)


pipeline(SAVE_REPOS_PATH)
