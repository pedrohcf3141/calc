from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from edukalculadora import app, manager


db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager.add_command("db", MigrateCommand)