import requests
import json
# GET ALL
URL = "http://127.0.0.1:8000/stuinfo/"
j = requests.get(URL)
py_data = j.text
print(py_data)

#GET 1
URL = "http://127.0.0.1:8000/stuinfo/2"
j = requests.get(URL)
py_data = j.text
print(py_data)



URL = "http://127.0.0.1:8000/add_student/"
data = {'name':'Havdahav',
        'age':40,
        'roll_no':20}
json_data = json.dumps(data)
j = requests.post(url=URL,data=json_data)
py_data = j.json()
print(py_data)