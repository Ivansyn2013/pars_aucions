from flask import Flask, render_template, jsonify, request
from views.table import table_app

from flask_migrate import Migrate
from commands.my_commands import my_commands_app
from views.auth import auth_app, login_manager
from views.project import project_app
from models.init_db import db
from logic.common_main import get_data
from dotenv import load_dotenv
import os
from jinja2 import Environment
from logic.addition_func import get_user_attribute

from config.config import DevelopmentConfig

load_dotenv()
config_class = os.getenv("CONFIG_CLASS")

# Create app
app = Flask(__name__)

# Blueprints
app.register_blueprint(table_app)
app.register_blueprint(my_commands_app)
app.register_blueprint(auth_app, url_prefix="/auth")
app.register_blueprint(project_app, url_prefix='/projects')

# Config
app.config.from_object(f'config.config.{config_class}')

# Database
db.init_app(app)
migrate = Migrate()
migrate.init_app(app, db, compare_type=True)

# Auth
login_manager.init_app(app)

# jinja
env = Environment()
env.globals.update(getattr=get_user_attribute)


@app.route('/')
def index():  # put application's code here
    return render_template('main/index.html')


@app.route('/execute_get_data', methods=['POST'], endpoint='execute_get_data')
def execute_get_data(claim_number=None):
    if claim_number is None:
        data = request.get_json()
        data = get_data(claim_number=data['claim_number'])
        data['status'] = 'ok'
        return jsonify(data)
    else:
        result = get_data(claim_number=claim_number)
        result['status'] = 'ok'
        return jsonify(result=result)
