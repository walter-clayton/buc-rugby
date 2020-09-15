# What I did so far with HEROKU

I folowed most of the set up from PART 1 of this website. The difference is that I added both nodejs and python buildpacks because I have already linked VUEJS and FLASK.

https://realpython.com/flask-by-example-part-1-project-setup/

## STEP 1

### Shell
```
touch Procfile
python -m pip install gunicorn
python -m pip freeze > requirements.txt
```
### Procfile
```
web: gunicorn app:app
```

## STEP 2

- create a file called `runtime.txt` and add python version bellow
```
python-3.8.2
```
## STEP 3

```
heroku create afitpilot-pro
heroku create afitpilot-stage
```
```
git remote add pro git@heroku.com:afitpilot-pro.git
git remote add pro git@heroku.com:afitpilot-stage.git
```
```
heroku buildpacks:add --index 1 heroku/nodejs --app afitpilot-stage
```
```
heroku buildpacks:add --index 2 heroku/python --app afitpilot-stage
```
```
git push stage master
git push pro master
```
## STEP 4
Create the `.env` file with the bellow text
```
source env/bin/activate
export APP_SETTINGS="config.DevelopmentConfig"
```
## STEP 5
Set up the staging and production environments for HEROKU.
```
heroku config:set APP_SETTINGS=config.StagingConfig --remote stage
heroku config:set APP_SETTINGS=config.ProductionConfig --remote pro
```
## STEP 6
Commit and push to test it out...
```
heroku run python app.py --app afitpilot-stage
heroku run python app.py --app afitpilot-pro
```

## NOTES
It's a bit complicated to set up HEROKU at this stage because I have already set up VUEJS and FLASK. I've already built an axios link. I am working on linking the Postgres database now. 
I will deploy properly once database works. 

Could check out this link that has used VUEJS + FLASK + HEROKU
- https://github.com/gtalarico/flask-vuejs-template
Also about HEROKU multiple Buildpacks
- https://devcenter.heroku.com/articles/buildpacks