# The simple is just the beginning to open your mind of how everything works in a simple way. "GuiDeLuccaDev"

'''
    
'''

import requests

def get_apm():
    api_key = "your rest api key"
    url = "https://api.newrelic.com/v2/applications.json"
    headers = {"X-Api-Key": api_key}

    response = requests.get(url, headers=headers)
    print(response.json())
    
get_apm()