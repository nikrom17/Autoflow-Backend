from flask import Flask
from flask_cors import CORS

from .routes import api
from .commands import create_tables, drop_and_create_tables, init_data
from .extensions import db

def create_app(config_file='settings.py'):
    app = Flask(__name__)
    
    app.config.from_pyfile(config_file)
    
    db.init_app(app)
    
    app.register_blueprint(api)
    
    CORS(app)
    
    # flask create_tables
    app.cli.add_command(create_tables)
    
    # flask drop_and_create_tables
    app.cli.add_command(drop_and_create_tables)
    
    # flask init_data
    app.cli.add_command(init_data)
    
    return app