# backend

## Update requirements
```
$ python -m pip freeze > requirements.txt
$ pip install -r requirements.txt 
```

## Project setup
```
$ python3 -m pip install --user virtualenv
$ python3 -m venv env
$ export FLASK_APP=app.py
$ source env/bin/activate
```

### Compiles and hot-reloads for development

```
(env)$ flask run
or 
(env)$ python app.py
```

### Data migragtion

```
(env)$ python manage.py migrate
or 
(env)$ python manage.py makemigration
```

### POSTGRESQL
```
sudo -u postgres psql

\l

\c mydatabase

\d table_name
```
### SQLALCHEMY
```
python
```
