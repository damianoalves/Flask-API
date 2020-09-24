from flask_migrate import MigrateCommand
from flask_script import Manager
from app import app

manager = Manager(app)

# Database migrations command
manager.add_command('db', MigrateCommand)
app.logger.debug('debug message')
app.logger.info('info message')
app.logger.warning('warn message')
app.logger.error('error message')
app.logger.critical('critical message')
if __name__ == '__main__':
    manager.run()
