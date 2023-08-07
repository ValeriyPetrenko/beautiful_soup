from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas 
# Импортируем необходимые библиотеки.
driver = webdriver.Chrome()
driver.implicitly_wait(30)
# Настраиваем работу Selenium, передав время ожидания до загрузки необходимых элементов.
url = "https://droider.ru/"
response = requests.get(url)
print(response)
# Задаём переменную с URL адресом, передаём в Requests для получения ответа от сервера.
driver.get(url)
driver.find_element(By.CLASS_NAME, "feed__continue").click()
driver.find_element(By.CLASS_NAME, "feed__continue").click()
# Передаём вебдрайверу URL, прокликиваем кнопку "Показать ещё", чтобы загрузить больше новостей.
html = driver.page_source
# Сохраняем HTML-код страницы.
soup = BeautifulSoup(html,'html.parser')
driver.quit()
# Передаём всё в BeautifulSoup, указываем парсер и закрываем вебдрайвер.
news = []
view_counter = []
# Создаём пустые списки, чтобы потом добавить туда полученные данные.
titles = soup.find_all('strong', class_= 'post-link__title')
for title in titles:
    delete_tags = title.get_text()
    news.append(delete_tags)
# Ищем названия новостей в коде страницы. В цикле for очищаем текст от HTML тегов и добавляем полученное в список.
counter = soup.find_all('span', class_= 'post-link__counter__view')
for number in counter:
    without_tags = number.get_text()
    view_counter.append(without_tags)
# Аналогично с предыдущим циклом делаём всё так же с счётчиком просмотров новостей.
result = dict({'Новость': news,'Количество просмотров': view_counter})
df = pandas.DataFrame(result)
df.to_csv('C:\Проекты\droider')
# Создаём словарь из двух списков и сохраняем результат в необходимой директории.
    