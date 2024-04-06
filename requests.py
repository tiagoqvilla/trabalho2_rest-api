import requests
import json

# TODO adicionar rota base
BASE_URL = ''


def fetch_all():
    res = requests.get(BASE_URL)
    data = json.loads(res.content)
    print(data)

def fetch_by_id(id):
    res = requests.get(BASE_URL + id)
    data = json.loads(res.content)
    print(data)

# TODO adicionar outras requests


if __name__ == '__main__':
    fetch_all()


