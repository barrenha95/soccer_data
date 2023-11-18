# RAPIDAPI : https://api-football-v1.p.rapidapi.com/v3/
# API-SPORTS : https://v3.football.api-sports.io/

# requests: 100 / day + $0.005 for each request over

import requests

url = "https://api-football-v1.p.rapidapi.com/v3/timezone"

key = ""

def get_api_response(url, key):
    url = url
    key = key
    headers = {
        "X-RapidAPI-Key":key,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    return response


response = get_api_response(url, key)
print(response.json())