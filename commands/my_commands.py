from flask import Blueprint
from models.users import Users
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
    admin = Users(user_name='admin', is_staff=True)
    db.session.add(admin)
    db.session.commit()
    print(Fore.GREEN + f'User added {admin}' + Fore.RESET)
