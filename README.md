pyton 3.5 + pytest + selenium
1. Создаем virtualenv.
 ```python3 -m venv env```
2. Обновляем pip
 ```pip install -U pip```
3. Устанавливаем зависимости
 ```pip install -r requirements.txt```
4. Проверяем установку командой ```pytest```
5. Скачиваем chromedriver с https://chromedriver.chromium.org/ , подкладываем в папку tests
6. Для отчетности можем использовать pytest-html либо allure, обе библиотеки установятся из requirements
7. Для примера можно запустить тесты, сформировать отчет allure и открыть его в окне браузера:
``` py.test --alluredir=%allure_result_folder% ./tests || allure serve %allure_result_folder% ```