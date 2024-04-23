from flask import Flask, abort, jsonify, render_template, request  # Импорт необходимых модулей
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)  # Создание экземпляра приложения Flask


def parse_content(url):
    data = {"title": "", "content": []}  # Создание словаря для хранения данных

    try:  # Обработка исключений для запросов
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            # Извлечение заголовка
            data["title"] = soup.title.string if soup.title else ""

            # Извлечение контента
            for tag in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p"]):
                content = {"tag": tag.name, "text": tag.text.strip()}
                data["content"].append(content)

    except requests.RequestException as e:  # Обработка ошибок запросов
        print(f"Error during requests to {url}: {str(e)}")

    return data


@app.route("/", methods=["GET", "POST"])  # Маршрут для главной страницы
def home():
    if request.method == "POST":  # Проверка метода запроса
        url = request.form["url"]  # Получение URL из формы
        if url:  # Проверка наличия URL
            parsed_data = parse_content(url)  # Парсинг контента
            return render_template(
                "index.html", data=parsed_data, url=url
            )  # Возврат шаблона с данными
        else:
            return render_template(
                "index.html", error="Введите URL.", url=""
            )  # Возврат шаблона с ошибкой
    return render_template("index.html", url="")  # Возврат пустого шаблона


@app.route('/api', methods=['GET'])
def api():
    url = request.json.get('url', None)
    if url:
        parsed_data = parse_content(url)
        print(type(parsed_data), parsed_data)
        return jsonify(parsed_data)
    abort(400)


if __name__ == "__main__":
    app.run(debug=True)
