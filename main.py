import datetime
import uuid
from urllib import response
from typing import List
from fastapi import FastAPI
import databases
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from pydantic import BaseModel

DATABASE_URL ="postgresql://drxtvgxmxkicix:06decdbd37e6b6a1f78453059699d5ec0ef463e13917f59c4f3b7b7f7b181a7f@ec2-34-227-135-211.compute-1.amazonaws.com:5432/d5u95l156m8uvf"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

events = sqlalchemy.Table(
    "eventdetails",
    metadata,
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("description",sqlalchemy.String),
    sqlalchemy.Column("date",sqlalchemy.String),
    sqlalchemy.Column("location",sqlalchemy.String),
    sqlalchemy.Column("category",sqlalchemy.String),
    sqlalchemy.Column("sponsors",sqlalchemy.String)

)

engine = sqlalchemy.create_engine(
    DATABASE_URL
)
metadata.create_all(engine)



app = FastAPI()



class Event(BaseModel):
    name: str
    date: datetime.datetime
    description: str
    location: str
    category: str
    sponsors: str



class EventEntry(BaseModel):
    name: str
    #date: str
    description: str
    location: str
    category: str
    sponsors: str

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

#To get event details

@app.get("/get-event/",response_model=List[Event])
async def get_event():
    query = events.select()
    return await database.fetch_all(query)
# To add event
@app.post("/create-event/", response_model=Event)
async def create_event(event:EventEntry):

    gDate = datetime.datetime.now()
    query = events.insert().values(
        name=event.name,
        description=event.description,
        date=gDate,
        location=event.location,
        category=event.category,
        sponsors=event.sponsors,)
    await database.execute(query)
    return {**event.dict()}


