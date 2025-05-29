# Указываем базовый образ
FROM kuchaser/myapp
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PYTHONPATH=/app

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл с зависимостями и устанавливаем их
RUN pip install poetry
COPY ./pyproject.toml ./
RUN poetry install --no-root


# Копируем код
COPY . .

EXPOSE 8000

# Запускаем сервер

#CMD ["python", "manage.py", "runserver"]
