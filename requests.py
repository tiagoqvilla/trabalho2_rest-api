import requests
import json

BASE_URL = ''


def fetch_all():
    res = requests.get(BASE_URL)
    data = json.loads(res.content)
    print(data)

def fetch_by_id(id):
    res = requests.get(BASE_URL + id)
    data = json.loads(res.content)
    print(data)



