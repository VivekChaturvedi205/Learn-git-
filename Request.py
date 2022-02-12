# GET REQUEST
import requests
import json
URL="http://localhost:8000/"

r=requests.get(url=URL)
data=r.json()
print(data)

# POST REQUEST

URL = "http://localhost:8000/stucreate/"
data = {
    'Name': 'Sonam',
    'Roll_no': 101,
    'City': "Khalilabad"
}
json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)
data = r.json()
print(data)
