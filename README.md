# Учебный проект: CI и CD проекта api_yamdb


## Автор - Домнина Анастасия


## Стек технологий
[![Django-app workflow](https://github.com/foxygen-d/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/foxygen-d/yamdb_final/actions/workflows/yamdb_workflow.yml)
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=56C0C0&color=008080)](https://www.postgresql.org/)
[![JWT](https://img.shields.io/badge/-JWT-464646?style=flat&color=008080)](https://jwt.io/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat&logo=NGINX&logoColor=56C0C0&color=008080)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat&logo=gunicorn&logoColor=56C0C0&color=008080)](https://gunicorn.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)
[![Docker-compose](https://img.shields.io/badge/-Docker%20compose-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)
[![Docker Hub](https://img.shields.io/badge/-Docker%20Hub-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/products/docker-hub)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat&logo=Yandex.Cloud&logoColor=56C0C0&color=008080)](https://cloud.yandex.ru/)


## Задача
Настроить для приложения Continuous Integration и Continuous Deployment, то есть реализовать:
* автоматический запуск тестов,
* обновление образов на Docker Hub,
* автоматический деплой на боевой сервер при пуше в главную ветку main.


## Шаблон наполнения env-файла
DB_ENGINE=django.db.backends.postgresql

POSTGRES_DB=infra_postgres

POSTGRES_USER=postgres

POSTGRES_PASSWORD=admin

POSTGRES_HOST=db

DB_PORT=5432


## Описание команд для запуска приложения в контейнерах
`docker build -t <имя образа> .` сборка образа

`docker run --name <имя контейнера> -it -p 8000:8000 yamdb` запуск контейнера

`docker-compose up` запуск docker-compose

`docker-compose up -d --build` запуск docker-compose с пересборкой контейнера


## Описание команд для заполнения базы данными
`python manage.py dumpdata > dump.json` экспорт данных в файл

`scp dump.json foxygen-d@158.160.2.148:/home/foxygen-d/yatube-website/yatube/` копирование файла dump.json с локального компьютера на сервер

Перенос данных с SQLite на PostgreSQL:
```
python3 manage.py shell
>>> from django.contrib.contenttypes.models import ContentType
>>> ContentType.objects.all().delete()
>>> quit()
```

`python manage.py loaddata dump.json` 