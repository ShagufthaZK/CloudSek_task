from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from application import app, db


migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def create_db():
    db.create_all()
    db.session.commit()

@manager.command
def drop_db():
    db.drop_all()

if __name__ == '__main__':
    manager.run()