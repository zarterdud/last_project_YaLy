import requests
from json import loads



def take_ans_request(url):
    response = requests.get('http://127.0.0.1:5000/api', url=url)
