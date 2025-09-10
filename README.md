#       `shards`
##      Criação do banco de dados
###     Instalação Postgresql
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib libpq-dev
```

###     Configuração inicial do banco de dados
```bash
sudo -u postgres psql

CREATE DATABASE myprojectdb;
CREATE USER myprojectuser WITH PASSWORD 'mypassword';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myprojectdb TO myprojectuser;
\q
```

##      Instalação dos requerimentos do projeto
```bash
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

##      Projeto Django
###     Criação do projeto
```bash
django-admin startproject myproject
cd myproject
```

###     Configuração inicial do projeto
```bash
python manage.py migrate
python manage.py createsuperuser
```

###     Inicia o servidor
```bash
python manage.py runserver
```

###     Cria uma aplicação Django
```bash
python manage.py startapp myapp


>>> INSTALLED_APPS = [
    ...
    'rest_framework',  # DRF for APIs
    'myapp',
]

```

#   Tutorial
Perfect! Let’s make a clean step-by-step setup script for a fresh Django + PostgreSQL environment, including the DB, user, schema privileges, and migrations. This assumes:

PostgreSQL 17 is installed and running on port 5434

Your project root is /home/nrdc/projects/shards/shards

You’re using a virtual environment (venv)

1️⃣ Create database and user with proper privileges
```bash
# 1. Connect as PostgreSQL superuser
sudo -u postgres psql -p 5434

# Inside psql:
-- Create the database
CREATE DATABASE myprojectdb;

-- Create a user with password
CREATE USER myprojectuser WITH PASSWORD 'mypassword';

-- Grant all privileges on the database
GRANT ALL PRIVILEGES ON DATABASE myprojectdb TO myprojectuser;

-- Connect to the database
\c myprojectdb

-- Grant privileges on the public schema
GRANT ALL PRIVILEGES ON SCHEMA public TO myprojectuser;
ALTER SCHEMA public OWNER TO myprojectuser;

-- Exit psql
\q
```

2️⃣ Configure Django settings

In shards/settings.py, set your database:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myprojectdb',
        'USER': 'myprojectuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5434',
    }
}
```

3️⃣ Install dependencies in the virtual environment

```bash
# Activate your venv
source venv/bin/activate

# Install Django, PostgreSQL driver, and DRF
pip install django psycopg2-binary djangorestframework
```
Optional: put them in requirements.txt so you can do pip install -r requirements.txt.

4️⃣ Create Django apps (Notes, Registers, Tags)

```bash
python manage.py startapp notes
python manage.py startapp registers
python manage.py startapp tags
```

Add all apps to INSTALLED_APPS in settings.py:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'notes',
    'registers',
    'tags',
]
```

5️⃣ Run migrations

```bash
# Make migrations for your apps
python manage.py makemigrations

# Apply all migrations
python manage.py migrate
```

6️⃣ Create superuser

```bash
python manage.py createsuperuser
```

7️⃣ Run the server

```bash
python manage.py runserver
```

Check http://127.0.0.1:8000/admin.