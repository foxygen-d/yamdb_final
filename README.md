# Учебный проект: CI и CD проекта api_yamdb


## Автор - Домнина Анастасия

![example workflow](https://github.com/github/docs/actions/workflows/yamdb_workflow.yml/badge.svg)

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