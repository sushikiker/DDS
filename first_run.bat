# 1. Установка зависимостей
pip install -r requirements.txt

# 2. Создание и применение миграций
python manage.py makemigrations
python manage.py migrate

# 3. Загрузка начальных данных (типы, категории, подкатегории и т.д.)
python load_init_data.py

# 4. Запуск сервера 
python manage.py runserver 127.0.0.1:8080
