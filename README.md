# Тестовое задание для компании «Азбука Мебели»


#### Как развернуть проект?

**а) С помощью Docker**

    docker-compose up -d

**б) Вручную**

- Запустить СУБД PostgreSQL на порту 5432.
- Создать пользователя *postgres* с паролем *postgres*.
- Создать базу *postgres* и выдать права пользователю *postgres*.

Выполнить команды:

    pip install -r requirements.txt
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py runserver
    
*Запущенный сервер доступен по адресу 127.0.0.1:8000*


## Скриншоты

<p align="center">
  <img src="https://github.com/EvilPug/furniture_analysis/raw/master/screenshots/category_select.png" />
</p>

<p align="center">
  <img src="https://github.com/EvilPug/furniture_analysis/raw/master/screenshots/graph_1.png" />
</p>

<p align="center">
  <img src="https://github.com/EvilPug/furniture_analysis/raw/master/screenshots/graph_2.png" />
</p>

<p align="center">
  <img src="https://github.com/EvilPug/furniture_analysis/raw/master/screenshots/graph_3.png" />
</p>

