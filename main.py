from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def parse_content(url):
    data = {
        "title": "",
        "texts": [],
        "links": {
            "internal": [],
            "external": []
        }
    }

    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Извлечение заголовка
            data["title"] = soup.title.string if soup.title else ""

            # Извлечение текстов
            for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']):
                data["texts"].append(tag.text.strip())

            # Извлечение ссылок
            domain = request.url_root
            for link in soup.find_all('a', href=True):
                href = link['href']
                if href.startswith('/') or (domain and href.startswith(domain)):
                    data["links"]["internal"].append((link.text.strip(), href))
                else:
                    data["links"]["external"].append((link.text.strip(), href))

    except requests.RequestException as e:
        print(f"Error during requests to {url}: {str(e)}")

    return data

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        if url:
            parsed_data = parse_content(url)
            return render_template('index.html', data=parsed_data, url=url)
        else:
            return render_template('index.html', error="Введите URL.", url="")
    return render_template('index.html', url="")

if __name__ == '__main__':
    app.run(debug=True)
