# Указываем базовый образ
FROM kuchaser/myapp:04e74c1925eed3fda3bb9f31f24d6c7b882422a9
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
