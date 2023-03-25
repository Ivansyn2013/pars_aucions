from flask import Flask, render_template, jsonify
from views.table import table_app

from flask_migrate import  Migrate
from commands.my_commands import my_commands_app
from views.auth import auth_app, login_manager
from views.project import project_app
from models.init_db import db
from logic.common_main import get_data
from dotenv import load_dotenv
import os

from config.config import DevelopmentConfig

load_dotenv()
config_class = os.getenv("CONFIG_CLASS")
#Create app
app = Flask(__name__)

#Blueprints
app.register_blueprint(table_app)
app.register_blueprint(my_commands_app)
app.register_blueprint(auth_app, url_prefix="/auth")
app.register_blueprint(project_app, url_prefix='/projects')

#Config
app.config.from_object(f'config.config.{config_class}')

#Database
db.init_app(app)
migrate = Migrate()
migrate.init_app(app, db, compare_type=True)

#Auth
login_manager.init_app(app)

@app.route('/')
def index():  # put application's code here
    return render_template('main/index.html')

@app.route('/execute_get_data', methods=['POST'])
def execute_get_data(claim_number):
    print(claim_number)
    result = get_data(claim_number=claim_number)
    return jsonify(result=result)


