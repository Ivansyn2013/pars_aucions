
from flask_login import UserMixin
from init_db import db
from sqlalchemy import Column, String, Integer, UUID, Boolean

class Users(db.Model, UserMixin):
    id = Column(UUID, unique=True, autoincrement=True, primary_key=True)
    user_name = Column(String(80), unique=True, nullable=False)
    is_staff = Column(Boolean,nullable=False,default=False)

    def __repr__(self):
        return f': User {self.user_name} # {self.id} :'