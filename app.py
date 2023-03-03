from flask import Flask, render_template
from views.table import table_app
from config.config import DevelopmentConfig
from commands.my_commands import my_commands_app
from views.auth import auth_app

#Create app
app = Flask(__name__)

#Blueprints
app.register_blueprint(table_app, url_prefix='/')
app.register_blueprint(my_commands_app)
app.register_blueprint(auth_app, url_prefix="/auth")

#Config
app.config.from_object(DevelopmentConfig)


@app.route('/')
def index():  # put application's code here
    return render_template('main/index.html')




