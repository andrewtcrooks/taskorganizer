[![Build Status](https://travis-ci.org/andrewtcrooks/taskorganizer.svg?branch=master)](https://travis-ci.org/andrewtcrooks/taskorganizer)

[![Coverage Status](https://coveralls.io/repos/github/andrewtcrooks/taskorganizer/badge.svg?branch=master)](https://coveralls.io/github/andrewtcrooks/taskorganizer?branch=master)


 # Task Organizer

Simple task list written in django


## Screenshots

<!--adding {attach} like this ({attach}screenshot*.jpg) -->


![Sign-in/Login](screenshot1.jpg?raw=true "Sign-in/Login")

![Task List](screenshot2.jpg?raw=true "Task List")

![Add Task](screenshot3.jpg?raw=true "Add Task")

![Edit Task](screenshot4.jpg?raw=true "Edit Task")


## Getting Started

These instructions will get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Python dependancies
```
Python==3.6.2
Django==1.11.5
```




Additional requirements
```
1. A locally served PostgreSQL database. I used the Postgres.app on my Mac but 
   any postgresql server should be fine.

2. Web browser open to http://127.0.0.1:8000
```


Optional requirements (goes with PostgreSQL database reset example below)
If you use Postgres.app on Mac, add the following lines to your .bashrc or .profile to enable CLI tools for the PostgreSQL database
```
# add CLI tools for PostGRESQL
export PATH="/Applications/Postgres.app/Contents/Versions/latest/bin:$PATH"
```

### Installing

After copying the repo you will need to create two files

Create local.py in settings directory (/taskorganizer/config/settings) with the following code and replace name_of_postgresql_db with the name of your PostgreSQL database
```
from .base import *

# JSON-based secrets module
with open('secrets.json') as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    """Get the secret variable or return explicit exception."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = 'Set the {0} environment variable'.format(setting)
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret('SECRET_KEY')

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'name_of_postgresql_db',
        'HOST': 'localhost',
    }}


INSTALLED_APPS += ['debug_toolbar',
                   ]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

```

Create secrets.json in root directory (/taskorganizer/) with the following code and replace your_key_here with a secret key that only you will know
```
{
  "FILENAME": "secrets.json",
  "SECRET_KEY": "your_key_here",
  "DATABASES_HOST": "127.0.0.1",
  "PORT": "5432"
}
```

For version control, make sure local.py and secrets.json are listed in your .gitignore file

Start the app on a local server by running the following code in a terminal and view at http://127.0.0.1:8000

```
cd ~/taskorganizer          # cd to wherever you put the repo locally
python manage.py runserver 8000 --settings=config.settings.local
```

You should now have a running version of the app!

Try adding/editing/deleting tasks and enjoy


### Resetting

Whenever you change the model you will need to first reset the database and then redo the migrations

To reset the database, run the following code in a terminal and replace db_name with the name of your PostgreSQL database
```
dropdb name_of_postgresql_db
create name_of_postgresql_db
```

To redo the migrations, delete the 0001_initial.py file in the /tasklist/app/migrations folder and run the following code in a terminal
```
python manage.py makemigrations --settings==config.settings.local
python manage.py migrate --settings==config.settings.local
```


## Built With

* [Django](https://docs.djangoproject.com/en/1.11/) - web framework

## Authors

* **Andrew T. Crooks** - [Github](https://github.com/andrewtcrooks)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


