import requests

def get_api_response(url, headers, params = ''):
    url = "https://api-football-v1.p.rapidapi.com/v3/"+url
    headers = headers

    if params != '':
        response = requests.get(url, headers=headers, params=params)    
    else:
        response = requests.get(url, headers=headers)
        
    return response

# Debug part
## If you don't change the key, the expected return is:
## "{'message': 'You are not subscribed to this API.'}"
if __name__ == '__main__':

    headers = {
        "X-RapidAPI-Key":"add_your_key_here_or_bad_request",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    response = get_api_response(url = 'timezone/', headers=headers)
    print(response.json())
    
