import requests


url = "https://wiki.archlinux.org/title/Installation_guide"
response = requests.get("http://lung-cancer-ai-gpt35.ru/api", json={"url": url}).json()
ans = f'Найденая информация:\nЗаголовок страницы: {response["title"]}\nКонтент: {response["content"][2]["text"]}\n{response["content"][3]["text"]}\n{response["content"][4]["text"]}'
print(ans)
