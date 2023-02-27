from flask import Flask, render_template
from views.table import table_app
app = Flask(__name__)
app.register_blueprint(table_app, url_prefix='/')

@app.route('/hi_world')
def hello_world():  # put application's code here
    return 'Hello World!'




