# conftest.py
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
django.setup()
