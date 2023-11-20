# RAPIDAPI : https://api-football-v1.p.rapidapi.com/v3/
# API-SPORTS : https://v3.football.api-sports.io/

# requests: 100 / day + $0.005 for each request over

from modules import requestModels
import time

key = "add_your_key_here_or_bad_request" #Key used for authentication
endpoint = requestModels.endpoints(key) #Create the object responsible to make the requests

print("timezones output:")
response = requestModels.endpoints.timezones(key = key)
print(response.json())
time.sleep(5)

print("injuries output:")
response = requestModels.endpoints.injuries(key = key, season = 2020, league = 61)
print(response.json())
time.sleep(5)

print("teams stats output:")
response = requestModels.endpoints.teams_stats(key = key, season = 2020, league = 71, team = 121)
print(response.json())
time.sleep(5)

print("teams info output:")
response = requestModels.endpoints.teams(key = key, team = 121)
print(response.json())
time.sleep(5)

print("fixtures output:")
response = requestModels.endpoints.fixtures(key = key, season = 2023, league = 71, round = 33)
print(response.json())
time.sleep(5)

print("leagues:")
response = requestModels.endpoints.leagues(key = key, country = 'Brazil')
print(response.json())