from bs4 import BeautifulSoup
import requests
import pandas 
# Импортируем необходимые библиотеки.
url = "https://www.ixbt.com/mobile/"
response = requests.get(url)
print(response)
# Проверяем с помощью Requests ответ от сервера.
dates_list = []
titles_list = []
# Заранее создаём пустые списки, чтобы потом добавить в них данные, полученные с сайта.
soup = BeautifulSoup(response.text, 'html.parser')
# Создаём "Красивый Суп", указывая необходимый парсер. 
news = soup.find_all('a', class_= 'item__text--title')
# Заранее посмотрев HTML-код страницы находим местонахождение заголовков новостей.
for titles in news:
    t = titles.text
    titles_list.append(t)
# В цикле for очищаем каждую новость от HTML-тегов. Далее добавляем полученные данные в список.
dates = soup.find_all('div', class_= 'info__date')
# Так же заранее изучив HTML-код страницы находим в нём даты публикации новостей.
for date in dates:
    d = date.text
    dates_list.append(d)
# В подобном цикле for делаем то же самое с датами публикации новостей.
result = dict({'Новость': titles_list, 'Дата публикации': dates_list})
# Создаем словарь из двух списков, с названями столбцов.
print(result)
# Проверяем получившиеся данные путём вывода через print.
df = pandas.DataFrame(result)
# Создаём датафрейм с помощью библиотеки Pandas.
df.to_csv('C:\Проекты\ixbt')
# Сохраняем результат в CSV файл в необходимую директорию.