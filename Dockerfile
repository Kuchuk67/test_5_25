FROM python:3.12
WORKDIR /app

# Устанавливаем Poetry
RUN pip install poetry==1.7.0

# Копируем зависимости
COPY pyproject.toml poetry.lock* ./

# Устанавливаем пакеты
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Копируем код
COPY . .

EXPOSE 8000

# Запускаем сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
