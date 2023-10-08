```python
import requests
import json
from utils import parse_json

def get_toast_api_data():
    url = "https://api.toast.com/data"
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers)
    return response.json()

def post_to_deskera(data):
    url = "https://api.deskera.com/data"
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(data))
    return response.json()

def integrate_toast_deskera():
    toast_data = get_toast_api_data()
    parsed_data = parse_json(toast_data)
    response = post_to_deskera(parsed_data)
    return response
```