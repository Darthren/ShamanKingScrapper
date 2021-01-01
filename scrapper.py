from bs4 import BeautifulSoup as BS # библиотека для парсинга веб страница
from Spirit import Spirit
import requests # http запросы
import json # преоброзовние данные в формат JSON

URL = "https://shamanking.fandom.com/wiki/Category:Spirits"

response = requests.get(URL) # GET запрос на веб страничку

mainSoup = BS(response.text, "html.parser") # парсинг веб странички
spirits  = mainSoup.findAll("a", class_="category-page__member-link") # достаем все <a class="category-page__member-link"></a>
photos   = mainSoup.findAll("div", class_="category-page__member-left") # достаем все <div class="category-page__member-left"></div>

spiritsJson = {
    "entries": []
}

for i in range(len(spirits)):
    title = spirits[i].get("title") # достаем имя духа
    if (title == "Category:Human Class Spirits"): continue
    href  = spirits[i].get("href") # достаем ссылку на страничку духа
    tmp   = photos[i].findAll("img") # достаем ссылку на фотку духа
    if (len(tmp) > 0):
        photo = tmp[0].get("src")
    else:
        photo = "No photo"

    spirit = Spirit(title, href, photo)
    spiritsJson["entries"].append(spirit.toJson()) # сохраняем объект духа

with open("test.json", "w") as file:
    file.write(json.dumps(spiritsJson)) # записываем в файл результат
