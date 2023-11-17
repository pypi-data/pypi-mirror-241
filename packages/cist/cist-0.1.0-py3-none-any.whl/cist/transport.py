import requests

ENDPOINT = "https://cist.nure.ua/ias/app/tt"

def api_request(path):
    url = ENDPOINT + path
    #print(url)
    response = requests.get(url)

    if response.status_code == 200:
        if not response.content:
            return None
        return response.json()