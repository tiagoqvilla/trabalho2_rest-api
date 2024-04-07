import requests
import json

BASE_URL = 'https://frozen-margret-qndrecarvalho.koyeb.app/course'

NEW_COURSE = {
    "NO_CINE_AREA_DETALHADA": "Formação de Engenheiros de Software",
    "NO_CINE_AREA_ESPECIFICA": "Desenvolvimento de Software",
    "NO_CINE_AREA_GERAL": "Tecnologia",
    "NO_CURSO": "Engenhria de Software",
    "QT_VG_TOTAL": 231
}

UPDATE_DATA = {
    "QT_VG_TOTAL": 2310
}

def fetch_all_courses():
    res = requests.get(BASE_URL)
    data = json.loads(res.content)
    print(data)

def fetch_course_by_id(id):
    res = requests.get(BASE_URL + f"/{id}")
    data = json.loads(res.content)
    print(data)

def create_course():
    res = requests.post(BASE_URL, data=NEW_COURSE, headers={"Content-Type": "application/json"})
    data = json.loads(res.content)
    print(data)

def update_course(id):
    res = requests.put(BASE_URL + f"/{id}", data=UPDATE_DATA, headers={"Content-Type": "application/json"})
    data = json.loads(res.content)
    print(data)

def delete_course(id):
    res = requests.delete(BASE_URL + f"/{id}")
    data = json.loads(res.content)
    print(data)



if __name__ == '__main__':
    fetch_all_courses()
    fetch_course_by_id('764609')


