from flask_login import UserMixin
from models.init_db import db
from sqlalchemy import Column, String, Integer, Boolean, ARRAY, ForeignKey, Table, LargeBinary, DateTime
from sqlalchemy.orm import relationship, backref
from datetime import datetime
import flask_bcrypt

import uuid

_projects_indetifier = db.Table('projects_indetifier',
                            db.Column('user_id', String(300), ForeignKey('users.id', ondelete='cascade',)),
                            db.Column('project_id', String(300), ForeignKey('projects.id', ondelete='cascade'),)
                                )


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = Column(String(300), unique=True, primary_key=True, default=str(uuid.uuid4()))
    first_name = Column(String(80), unique=False, nullable=False)
    last_name = Column(String(80), unique=False, nullable=False)
    username = Column(String(80), unique=True, nullable=False, default='', server_default='')
    email = Column(String(200), unique=True, nullable=False)
    role = Column(ARRAY(String(80)), nullable=False, default='usual')
    _password = Column(LargeBinary, nullable=True)

    project = relationship('Project',  secondary=_projects_indetifier,
                               back_populates='user')
    log = relationship('Log', back_populates='user')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = flask_bcrypt.generate_password_hash(value)

    def validate_password(self, password) -> bool:
        return flask_bcrypt.check_password_hash(self._password, password)

    def __repr__(self):
        return f"< User {self.id} {self.first_name!r} {self.last_name} Ваш статус: {self.role}>"



class Log(db.Model):
    __tablename__ = 'logs'
    id = Column(String(300), unique=True, primary_key=True, default=str(uuid.uuid4()))
    user_id = Column(String, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='log')
class Project(db.Model):
    __tablename__ = 'projects'
    id = Column(String(300), unique=True, primary_key=True, default=str(uuid.uuid4()))

    name = Column(String(100), nullable=False)
    status = Column(String(100), nullable=False, default='active')
    created_at = Column(DateTime, default=datetime.utcnow())
    last_update = Column(DateTime, nullable=True)

    user = relationship('User',
                        secondary=_projects_indetifier,
                        back_populates='project')