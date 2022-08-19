# Учебный проект: CI и CD проекта api_yamdb


## Автор - Домнина Анастасия


## Стек технологий
[![Django-app workflow](https://github.com/foxygen-d/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/foxygen-d/yamdb_final/actions/workflows/yamdb_workflow.yml)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)
[![Docker-compose](https://img.shields.io/badge/-Docker%20compose-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)
[![Docker Hub](https://img.shields.io/badge/-Docker%20Hub-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/products/docker-hub)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat&logo=Yandex.Cloud&logoColor=56C0C0&color=008080)](https://cloud.yandex.ru/)


## Задача
Настроить для приложения Continuous Integration и Continuous Deployment, то есть реализовать:
* автоматический запуск тестов
* обновление образов на Docker Hub
* автоматический деплой на боевой сервер при пуше в главную ветку main


## Описание workflow
* проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8) и запуск pytest из репозитория yamdb_final
* сборка и доставка докер-образа для контейнера web на Docker Hub
* автоматический деплой проекта на боевой сервер
* отправка уведомления в Telegram о том, что процесс деплоя успешно завершился


## Запуск проекта

### Шаблон наполнения env-файла
```
DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=infra_postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
DB_PORT=5432
```

### Запуск docker-compose
`$ sudo docker-compose up -d --build`

### Выполнить миграции, создать суперпользователя, собрать статику, заполнить базу начальными данными
```
$ sudo docker-compose exec web python manage.py migrate
$ sudo docker-compose exec web python manage.py createsuperuser
$ sudo docker-compose exec web python manage.py collectstatic --no-input
$ sudo docker-compose exec web python manage.py loaddata fixtures.json
```

Проект доступен по [ссылке](http://51.250.106.125/admin)
