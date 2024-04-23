import requests


def take_ans_request(url):
    response = requests.get("http://127.0.0.1:5000/api", json={"url": url})
    if response.status_code == 200:
        return response.json()
    return {}
