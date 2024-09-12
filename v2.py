import requests
import json


def get_data(id=None):
    URL ="http://127.0.0.1:8000/"
    URL= URL + "employee_data/"
    data = {}
    if id is not None:
        data ={'id':id}
    json_data = json.dumps(data)
    response = requests.get(URL ,data = json_data)
    data = response.json()
    print(data)

get_data()
 