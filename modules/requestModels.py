import time

if __name__ == '__main__':
    import requestGet    
else:
    from modules import requestGet    

class endpoints():

    def __init__(self, key):
        self.key = str(key)

    def timezones(key):
        url = "timezone/"

        headers = {
            "X-RapidAPI-Key":str(key),
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }

        response = requestGet.get_api_response(url= url, headers = headers)
        return(response)
    
    def injuries(key, season, league):
        url = "injuries"
        params = {
            "season": str(season),
            "league": str(league)
        }

        headers = {
            "X-RapidAPI-Key":str(key),
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }

        response = requestGet.get_api_response(url= url, headers = headers, params=params)
        return(response)

    def teams_stats(key, season, league, team):
            url = "teams/statistics"
            params = {
                "season": str(season),
                "league": str(league),
                "team": str(team)
            }

            headers = {
                "X-RapidAPI-Key":str(key),
                "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
            }

            response = requestGet.get_api_response(url= url, headers = headers, params=params)
            return(response)
    
    def teams(key, team):
            url = "teams"
            params = {
                "id": str(team)
            }

            headers = {
                "X-RapidAPI-Key":str(key),
                "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
            }

            response = requestGet.get_api_response(url= url, headers = headers, params=params)
            return(response)    

    def fixtures(key, season, league, round):
            url = "fixtures"
            params = {
                "season": str(season),
                "league": str(league),
                "round": "Regular Season - " + str(round)
            }

            headers = {
                "X-RapidAPI-Key":str(key),
                "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
            }

            response = requestGet.get_api_response(url= url, headers = headers, params=params)
            return(response)
    
    def leagues(key, country):
            url = "leagues"
            params = {
                "country": str(country)
            }

            headers = {
                "X-RapidAPI-Key":str(key),
                "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
            }

            response = requestGet.get_api_response(url= url, headers = headers, params=params)
            return(response)    
    

##### Debugging #####
if __name__ == '__main__':


    key = "add_your_key_here_or_bad_request"    
    endpoint = endpoints(key=key)

## timezone ##
## If you don't change the key, the expected return is:
## "{'message': 'You are not subscribed to this API.'}"
    response = endpoint.timezones()
    print("timezone response: ")
    print(response.json())

    time.sleep(5)

## injuries ##
## If you don't change the key, the expected return is:
## "{'message': 'You are not subscribed to this API.'}"
    response = endpoint.injuries(season = 2020, league = 61)
    print("injuries response: ")
    print(response.json())

    time.sleep(5)

## team statistics ##
## If you don't change the key, the expected return is:
## "{'message': 'You are not subscribed to this API.'}"
    response = endpoint.teams_stats(season = 2020, league = 71, team = 121)
    print("team statistics response: ")
    print(response.json())      

    time.sleep(5)

## team info ##
## If you don't change the key, the expected return is:
## "{'message': 'You are not subscribed to this API.'}"
    response = endpoint.teams(team = 121)
    print("team info response: ")
    print(response.json())      

    time.sleep(5)

## fixtures ##
## If you don't change the key, the expected return is:
## "{'message': 'You are not subscribed to this API.'}"
    response = endpoint.fixtures(team = 121)
    print("team info response: ")
    print(response.json())      

    time.sleep(5)
                
## leagues ##
## If you don't change the key, the expected return is:
## "{'message': 'You are not subscribed to this API.'}"
    response = endpoint.leagues(team = 121)
    print("team info response: ")
    print(response.json())                   