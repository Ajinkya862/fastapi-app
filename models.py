import datetime

from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column
from .database import Base

class Job(Base):
    __tablename__ = "Jobs"

    id = Column(Integer, Primary_key=True)
    name = Column(String, Nullable= False)
    description = Column(String)
    date = Column(datetime.date)
    location = Column(String)
    category = Column(String)
    sponsors = Column(String)
