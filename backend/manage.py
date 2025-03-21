#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os  # Модуль для работы с переменными окружения
import sys  # Модуль для работы с аргументами командной строки


def main():
    """Run administrative tasks."""  # Главная функция для выполнения команд Django

    # Устанавливает настройки Django, если они ещё не заданы
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab1.settings')

    try:
        # Импортирует функцию для выполнения команд Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Выводит сообщение об ошибке, если Django не установлен или не найден
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Выполняет переданную команду (например, runserver, migrate)
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()  # Запускает main() при выполнении файла напрямую
