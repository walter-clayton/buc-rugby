# Deploying to heroku

1. change runtime to 
```
python-3.7.10
```

2. switch name run.py to app.py
also just use 
```
app.run(debug=True)
```

3. procfile 
```
web: gunicorn app:app
```
4. pip freeze > requirements.txt
remove useless packages if needed
removed pyinstaller

5. config.py
add all the dependencies from the .env file

6. add commit and push
```
git push heroku master
```
