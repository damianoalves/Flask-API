import os
from flask import Flask
from flask.logging import default_handler
from app import main
from app.main.api import api
from app.main.database import db, migration

# Flask App Initialization
app = Flask(__name__)
app.config.from_object(main.settings[os.environ.get('APPLICATION_ENV', 'default')])
app.logger.addHandler(default_handler)

# Database ORM Initialization
db.init_app(app)

# Database Migrations Initialization
migration.init_app(app, db)

# Flask API Initialization
api.init_app(app)
