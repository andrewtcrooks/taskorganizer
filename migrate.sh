#!/bin/bash
source django

# add CLI tools for PostGRESQL
export PATH="/Applications/Postgres.app/Contents/Versions/latest/bin:$PATH"

# Delete and recreate PostGRESQL database
dropdb andrew
createdb andrew

# Delete migration files
find /Users/andrew/git/taskorganizer/todolist -path "*/migrations/*.py" -not -name "__init__.py" -delete
find /Users/andrew/git/taskorganizer/todolist -path "*/migrations/*.pyc" -delete

# Recreate migration files and migrate
python manage.py makemigrations --settings=config.settings.local    
python manage.py migrate --settings=config.settings.local    

