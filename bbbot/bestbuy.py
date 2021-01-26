import requests
from bs4 import BeautifulSoup

headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

availability_str = '"availability":"http://schema.org/InStock"' 
nonavailability_str = '"availability":"http://schema.org/SoldOut"'

def get_request(endpoint):
    req = requests.get(endpoint, headers=headers)
    print("SENDING REQUEST")
    print(req.text)
    return req

def availability(endpoint):
    print(availability_str in get_request(endpoint).text)
    return availability_str in get_request(endpoint).text

