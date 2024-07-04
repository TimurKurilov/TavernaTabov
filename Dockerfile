# Используйте базовый образ Python
FROM python:3.8-slim

# Установите рабочую директорию в контейнере
WORKDIR /app

# Скопируйте файл requirements.txt в контейнер
COPY requirements.txt /app/

# Установите зависимости
RUN pip install -r requirements.txt

# Скопируйте содержимое директории main в рабочую директорию
COPY main/ /app/main/

# Укажите команду для запуска приложения
CMD ["gunicorn", "--chdir", "main", "--bind", ":8000", "main.wsgi:application"]
