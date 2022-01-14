from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

import config.env as env

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(env) #Alternative = 'config.env'
    app.config.from_envvar("PROJECTNAME_SETTINGS", silent=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = '{driver}://{user}:{password}@{host}:{port}/{database}?charset={charset}'.format(
    driver=app.config['DB_DRIVER'],
    user=app.config['DB_USER'],
    password=app.config['DB_PASSWORD'],
    host=app.config['DB_HOST'],
    port=app.config['DB_PORT'],
    database=app.config['DB_NAME'],
    charset=app.config['DB_CHARSET'],
    )
    if test_config:
        app.config.from_mapping(test_config)

    with app.app_context():
        # importing the migration, model, controller and route to make sure they are known to Flask-MVC
        from aplication.models import UserModel, ErbModel
        from aplication.controllers import UserController, ErbController 
        # Import parts of our application
        from aplication.routes import web

        # Register Blueprints
        app.register_blueprint(web.user)
        app.register_blueprint(web.erb)

    db.init_app(app)
    #csrf.init_app(app)
    Migrate(app, db)

    # any other registrations; blueprints, template utilities, commands
    return app