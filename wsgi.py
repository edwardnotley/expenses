import sys
import os

# Path to your project
sys.path.insert(0, "/var/www/expenses")

# Activate the virtual environment
activate_this = '/var/www/expenses/venv/bin/app.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from app import app as application
