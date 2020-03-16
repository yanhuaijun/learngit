#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_test.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#1.创建工程  django-admin startproject xxxx
#2.cd 进入xxxx目录下创建项目   python manage.py startapp app
#3.更新 命令  python manage.py makemigrations
#4.设置文件配置好数据库，同步数据库命令  python manage.py migrate
#5.启动项目 在xxxx 目录下运行 python manage.py runserver
