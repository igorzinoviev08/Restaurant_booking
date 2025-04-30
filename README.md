Restaurant Booking API

Проект представляет собой RESTful API для бронирования столиков в ресторане.
Описание

API предоставляет следующие возможности:

    Регистрация пользователей.
    Бронирование столиков на определенное время.
    Просмотр доступных столиков.
    Управление бронированиями (обновление, удаление).

Технологии

    FastAPI — веб-фреймворк для создания API.
    PostgreSQL — база данных.
    SQLAlchemy — ORM для работы с базой данных.
    Alembic — инструмент для миграций.
    Pytest — фреймворк для написания тестов.
    Loguru — библиотека для логгирования.
    Docker — контейнеризация приложения.

Архитектура

Проект разделен на следующие модули:

    api: Маршруты API.
    core: Настройки приложения (логгирование, конфигурации).
    models: SQLAlchemy модели.
    schemas: Pydantic схемы для валидации данных.
    services: Бизнес-логика приложения.
    tests: Юнит-тесты для проверки базовых сценариев.

Запуск проекта
1. Клонирование репозитория

git clone https://github.com/your-repo/restaurant_booking.git
cd restaurant_booking

Структура проекта:
rrestaurant_booking/
├**├── app/
│   ├── __init__.py
│   ├── main.py           # Основной файл приложения
│   ├── routers/          # Маршруты API
│   │   ├── __init__.py
│   │   ├── tables.py
│   │   └── reservations.py
│   ├── models/           # Модели SQLAlchemy
│   │   ├── __init__.py
│   │   └── base.py
│   ├── schemas/          # Pydantic модели для валидации
│   │   ├── __init__.py
│   │   ├── tables.py
│   │   └── reservations.py
│   ├── services/         # Бизнес-логика
│   │   ├── __init__.py
│   │   ├── tables.py
│   │   └── reservations.py
│   ├── database.py       # Настройка подключения к базе данных
│   ├── alembic.ini       # Конфигурация Alembic
│   └── migrations/       # Миграции Alembic
├── tests/                # Тесты pytest
│   ├── __init__.py
│   ├── test_tables.py
│   └── test_reservations.py
├── Dockerfile            # Dockerfile для FastAPI
├── docker-compose.yml    # Docker Compose для запуска PostgreSQL и FastAPI
└── requirements.txt      # Зависимости**

2.Установка зависимостей
Создайте файл requirements.txt: 

3.Установите зависимости:
pip install -r requirements.txt

4.Настройка базы данных  
Файл app/database.py: 

5.Модели SQLAlchemy  
Файл app/models/base.py: 

6.Pydantic модели  
Файл app/schemas/tables.py: 
Файл app/schemas/reservations.py:

7.Бизнес-логика  
Файл app/services/reservations.py: 

8.Маршруты  
Файл app/routers/tables.py: 
Файл app/routers/reservations.py:

9.Docker и Docker Compose  
Файл Dockerfile: 
Файл docker-compose.yml:

10.Запуск приложения  
bash
docker-compose up --build

10.Тестирование  
Файл tests/test_reservations.py: 


 


2.Установка зависимостей
Создайте файл requirements.txt: 

3.Установите зависимости:
pip install -r requirements.txt

4.Настройка базы данных  
Файл app/database.py: 

5.Модели SQLAlchemy  
Файл app/models/base.py: 

6.Pydantic модели  
Файл app/schemas/tables.py: 
Файл app/schemas/reservations.py:

7.Бизнес-логика  
Файл app/services/reservations.py: 

8.Маршруты  
Файл app/routers/tables.py: 
Файл app/routers/reservations.py:

9.Docker и Docker Compose  
Файл Dockerfile: 
Файл docker-compose.yml:

10.Запуск приложения  
bash
docker-compose up --build

10.Тестирование  
Файл tests/test_reservations.py: 


 

