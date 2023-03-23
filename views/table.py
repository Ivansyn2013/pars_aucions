from flask import Blueprint, render_template, request, jsonify
from logic.common_main import get_data
from flask_login import login_required
from sqlalchemy.exc import IntegrityError, DataError
from models.users import Auction
from models.init_db import db
from logs import my_loger
from datetime import datetime

table_app = Blueprint('table_app', __name__)


@table_app.route('/table/', methods=["GET", "POST"], endpoint='/table')
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


@table_app.route('/table/get_auction/', methods=["POST"], endpoint='get_auction')
@login_required
def send_auction_to_db():
    '''
    get data fron js and send in db , create auction obj
    return: status ok
    '''
    data = request.get_json()[0]

    auction = Auction()
    date_event_format = '%d.%m.%Y %H:%M'
    pub_date_format = '%a, %d %b %Y %H:%M:%S %Z'
    #данные аукциона
    auction.claim_number = int(*data['Номер закупки'])
    auction.claim_object = data['Наименование объекта закупки'][0]
    auction.pub_date = datetime.strptime(data['pub_date'][0].strip(), pub_date_format)
    auction.event_description = data['Описание события'][0]
    auction.event_date = datetime.strptime(data['Дата и время события'][0].strip(), date_event_format)

    try:
        db.session.add(auction)
        db.session.commit()
    except IntegrityError or DataError as error:
        my_loger.critical('Ошибка создания аукциона в бд. send_auction_to_db()\n')
        my_loger.critical(error)
        return jsonify({'status':'bad'})
    my_loger.info(f'Аукцион сохранен в бд - {Auction.query.filter_by(claim_number=auction.claim_number).first().id}')
    return jsonify({'status': 'ok'})
