from flask import Flask, render_template
from views.table import table_app
from config.config import DevelopmentConfig
from commands.my_commands import my_commands_app

#Create app
app = Flask(__name__)

#Blueprints
app.register_blueprint(table_app, url_prefix='/')
app.register_blueprint(my_commands_app)

#Config
app.config.from_object(DevelopmentConfig)


@app.route('/hi_world')
def hello_world():  # put application's code here
    return 'Hello World!'




