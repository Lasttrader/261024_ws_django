import requests

api_message = requests.post('http://127.0.0.1:5000/api/v1/get_data/')
if api_message.ok:
    print(api_message.json())