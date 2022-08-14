import datetime

from database import Base
from sqlalchemy import String,Integer,Column,Text
class Event(Base):
    __tablename__ = 'events'
    name = Column(String(255),nullable=False,primary_key=True)
    description = Column(Text)
    date= Column(Text)
    location = Column(String)
    category = Column(String)
    sponsors = Column(String)

