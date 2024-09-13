import requests
import json

URL ="http://127.0.0.1:8000/employee_api/"

def get_data(id=None):
    data = {}
    if id is not None:
        data ={'id':id}
    json_data = json.dumps(data)
    response = requests.get(URL ,data = json_data)
    data = response.json()
    print(data)

def post_data():
    data ={'name':'Rinku',
           'employee_id':42,
           'position':'chaprasi'
           }
    json_data = json.dumps(data)
    response = requests.post(URL,data = json_data)
    data = response.json()
    print(data)

def update_data():
    data ={'id':4,
           'name':'Rahul',
           'position':'Peon'
           }
    json_data = json.dumps(data)
    response = requests.put(URL,data = json_data)
    data = response.json()
    print(data)

def delete_data(id=None):
    data = {
        'id':id
    }
    json_data = json.dumps(data)
    response = requests.delete(URL,data=json_data)
    data = response.json()
    print(data)

delete_data(3)
get_data()