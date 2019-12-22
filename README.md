pyton 3.5 + pytest + selenium
1. Создаем virtualenv.
 ```python3 -m venv env```
2. Обновляем pip
 ```pip install -U pip```
3. Устанавливаем зависимости
 ```pip install -r requirements.txt```
4. Проверяем установку командой ```pytest```
5. Скачиваем chromedriver с https://chromedriver.chromium.org/ , подкладываем в папку tests
6. Для отчетности можем использовать pytest-html
 ```pip install pytest-html```
 ```pytest --html=report.html```
