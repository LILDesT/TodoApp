FROM python:3.9

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Обновляем pip и устанавливаем зависимости
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Запускаем приложение через uvicorn. Предполагается, что ваш файл называется main.py и объект приложения — app.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
