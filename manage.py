#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apiElectricalSystems.settings')
    try:
        from django.core.management import execute_from_command_line
        from django.core.management.commands.runserver import Command
        "Personalized code to runserver on my_preference to IP and Port Server"
        Command.default_addr = '192.168.1.253'
        Command.default_port = '5000'
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
