from flask_migrate import MigrateCommand
from flask_script import Manager
from app import app

manager = Manager(app)

# Database migrations command
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
