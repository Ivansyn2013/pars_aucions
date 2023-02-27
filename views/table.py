from flask import Blueprint, render_template
from logic.common_main import get_data
table_app = Blueprint('table_app', __name__)
@table_app.route('/', endpoint='/')
def table_render():
    data = get_data()
    return render_template('base.html',
                           data=data)