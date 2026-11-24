#!/usr/bin/env bash
# Выходим сразу, если команда завершилась с ошибкой
set -o errexit

# Устанавливаем зависимости
pip install -r requirements.txt

# Собираем статические файлы в папку staticfiles
python manage.py collectstatic --no-input

# Применяем миграции к базе данных
python manage.py migrate
