from flask import Blueprint, render_template, request
from logic.common_main import get_data
from flask_login import login_required
table_app = Blueprint('table_app', __name__)


@table_app.route('/table/', methods=["GET","POST"], endpoint='/table')
@login_required
def table_render():

    if request.method == "GET":
        data = get_data()
        return render_template('main/table.html',
                               data=data)
    elif request.method == "POST":
        data = get_data(request.form.get('claim_number'))
        return render_template('main/table.html',
                               data=data)
