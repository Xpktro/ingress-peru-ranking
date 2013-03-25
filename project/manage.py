#!/usr/bin/env python

from os.path import join
import os
import sys

import imp

try:
    imp.find_module('settings')  # Assumed to be in the same directory.
except ImportError:
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)

from settings import PROJECT_DIR
sys.path.insert(0, join(PROJECT_DIR, 'apps'))

# for directory in os.walk(APPS_DIR).next()[1]:
#     sys.path.insert(0, join(APPS_DIR, directory))

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
