from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
db.create_engine
migrate = Migrate(app, db)

from webapp.routes import user_route
from webapp.models import user_model