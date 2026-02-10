#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# تجميع الملفات الثابتة (CSS/JS)
python manage.py collectstatic --no-input

# تطبيق الترحيلات لقاعدة البيانات
python manage.py migrate