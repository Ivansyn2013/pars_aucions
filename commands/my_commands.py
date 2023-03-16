from flask import Blueprint
from models.users import User
from models.init_db import db
from colorama import Fore
import os

my_commands_app = Blueprint('my_command', __name__)


@my_commands_app.cli.command('init-db')
def init_db():
    '''CLI command for init db'''
    if os.path.exists('instance/db.db'):
        db.drop_all()
        print(Fore.YELLOW + 'Last database deleted' + Fore.RESET)
    db.create_all()
    print(Fore.GREEN + 'Db inited!!!' + Fore.RESET)


@my_commands_app.cli.command("create-user")
def create_user():
    '''
    Cli command for create Flask user in db
    > Created user: user
    '''
    if not User.query.filter_by(first_name='admin').one_or_none():
        admin = User()
        admin.email = 'example@ww.ru'
        admin.role = ['admin']
        admin.first_name = 'admin'
        admin.last_name = 'admin'
        admin.password = '123'
        db.session.add(admin)
        db.session.commit()
        print(Fore.GREEN + f'User added {admin}' + Fore.RESET)
    else:
        print(Fore.RED + f'User admin is exists' + Fore.RESET)

@my_commands_app.cli.command('drop_all')
def drop_all():
    '''CLI command for drop all tables in db'''

    db.drop_all()
    print(Fore.GREEN + 'Db Droped!!!' + Fore.RESET)
