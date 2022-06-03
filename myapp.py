import json
import requests

URL = "http://127.0.0.1:8000/squad/"


def post_data():
    data = {
        'name': 'Khan Tweleve Team',
        'members': 11,
        'color': 'Combination of Blue and Black'
    }

    json_data = json.dumps(data)
    response = requests.post(url=URL, data=json_data)
    data = response.json()
    print(data)


post_data()
