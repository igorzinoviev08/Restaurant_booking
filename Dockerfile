FROM python:3.11-slim

# Установка рабочей директории
WORKDIR /app

# Установка Poetry
RUN pip install poetry

# Копирование файлов конфигурации Poetry
COPY pyproject.toml poetry.lock* ./

# Настройка Poetry и установка зависимостей
RUN poetry config virtualenvs.create false && poetry install --no-root

# Копирование исходного кода приложения
COPY . .

# Команда для запуска приложения
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]