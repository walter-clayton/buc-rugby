# import os
# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand
# from app import app, db

# def get_env_variable(POSTGRES_URL):
#     try:
#         return os.environ[POSTGRES_URL]
#     except KeyError:
#         message = "Expected environment variable '{}' not set.".format(name)
#         raise Exception(message)

# # the values of those depend on your setup
# POSTGRES_URL = get_env_variable("POSTGRES_URL")
# POSTGRES_USER = get_env_variable("POSTGRES_USER")
# POSTGRES_PW = get_env_variable("POSTGRES_PW")

# app.config.from_object(os.environ['APP_SETTINGS'])

# migrate = Migrate(app, db)
# manager = Manager(app)

# manager.add_command('db', MigrateCommand)

# POSTGRES_DB = get_env_variable("POSTGRES_DB")

# if __name__ == '__main__':
#     manager.run()