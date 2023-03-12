import uuid

from flask_login import UserMixin

from models.users import projects_indetifier
from models.init_db import db
from sqlalchemy import Column, String, Integer,  Boolean, ARRAY, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


