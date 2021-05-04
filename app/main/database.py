from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Database ORM Configuration
db = SQLAlchemy()

# Database Migrations Configuration
migration = Migrate(directory='./app/migrations')