import requests


client_form = ['unemployed',
                           'married',
                           'primary',
                           'no',
                           'no',
                           'yes',
                           'cellular',
                           'may',
                           'failure',
                           30,
                           1787,
                           16,
                           199,
                           4,
                           330,
                           0]

api_message = requests.post('http://127.0.0.1:5000/api/v1/get_data/',
                            json = {'client_form': [client_form]})
if api_message.ok:
    print(api_message.json())