import requests


def take_ans_request(url):
    response = requests.get(
        "http://lung-cancer-ai-gpt35.ru/api", json={"url": url}
    ).json()
    ans = f'Найденая информация:\nЗаголовок страницы: {response["title"]}\nКонтент: {response["content"][2]["text"]}\n{response["content"][3]["text"]}\n{response["content"][4]["text"]}\nДля большей информации перейдите на сайт: \nhttp://lung-cancer-ai-gpt35.ru'
    return ans
