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
### DOCKER
```
To build the docker image 'part_9', long as you are in the same directory as the 'Dockerfile', would be:

docker build . --tag=part_9

To run the docker container using the image called 'part_9' requires:

docker run -p 5000:5000 part_9

To run the docker volume
docker run -p 5000:5000 -v $(pwd):/app docker-volume

docker-compose down
docker-compose up
``` 
