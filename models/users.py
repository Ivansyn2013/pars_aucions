
from flask_login import UserMixin
from models.init_db import db
from sqlalchemy import Column, String, Integer,  Boolean
import uuid

class Users(db.Model, UserMixin):
    id = Column(String(300), unique=True, primary_key=True, default=str(uuid.uuid4()))
    user_name = Column(String(80), unique=True, nullable=False)
    is_staff = Column(Boolean,nullable=False,default=False)

    def __repr__(self):
        return f': User {self.user_name} # {self.id} :'