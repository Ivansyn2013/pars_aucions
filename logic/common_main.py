import requests
from bs4 import BeautifulSoup
from models.init_db import db
from models.users import Auction
from sqlalchemy.exc import IntegrityError
from logs.init_logger import my_loger
def get_data(claim_number='0373100037223000034',
             url='https://zakupki.gov.ru/epz/order/notice/rss'):
    '''take number of claim and url
    :return text from url request'''

    HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0'}
    params = {'regNumber':claim_number}
    responce = requests.get(url, headers=HEADERS, params=params)

    print(responce.status_code)
    soup = BeautifulSoup(responce.text, features='xml')
    pub_date = soup.find('pubDate').text
    result = soup.find_all('description')
    print(len(result))

    for_dict = result[1].text.replace('<strong>','').\
        replace('</strong>','').split('<br/>')
    pairs_of_text = []
    for iteam in for_dict:
        if iteam:
            pairs_of_text.append(tuple(iteam.split(':',1)))

    dict_of_pairs = dict(pairs_of_text)
    dict_of_pairs['pub_date'] = pub_date
    return dict_of_pairs

def save_get_data_indb(claim_number):
    data = get_data(claim_number)
    auction = Auction()
    auction.claim_object = data['Наименование объекта закупки']
    auction.event_description = data['Описание события']
    auction.claim_number = data['Номер закупки']
    auction.pub_date = data['pub_date']
    auction.event_date = data['Дата и время события']
    db.session.add(auction)
    try:
        db.session.commit()
    except IntegrityError as error:
        my_loger.error(f'Ошибка из savegetdata {error}')
        return None
    my_loger.info('Сохранен новый аукцион в базе')
    return True

if __name__ == '__main__':
    print(get_data('0373100037223000034'))