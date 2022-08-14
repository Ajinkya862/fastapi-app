
from typing import List
from fastapi import FastAPI
from database import SessionLocal, engine
from pydantic import BaseModel
import models
models.Base.metadata.create_all(bind=engine)

app = FastAPI()



class Event(BaseModel):
    name       : str
    description: str
    date       : str
    location   : str
    category   : str
    sponsors   : str

    class Config:
        orm_mode=True



def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.on_event("startup")
# async def startup():
#     await database.connect()
#
# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()

#To get event details

@app.get('/get-event',response_model=List[Event])
async def get_all_events():
    events = db.query(models.Event).all()

    return events

@app.get('/get-event/{name}',response_model=Event)
async def get_by_name(name:str):
    byname = db.query(models.Event).filter(models.Event.name==name).first()
    return byname

@app.get('/get-event/{category}',response_model=Event)
async def get_by_cat(category: str):
    bycat = db.query(models.Event).filter(models.Event.category==category).first()
    return bycat

@app.post('/get-event/',response_model=Event)
async def create_event(event:Event):
    new_event = models.Event(
        name= event.name,
        description = event.description,
        date = event.date,
        location = event.location,
        category = event.category,
        sponsors= event.sponsors
    )

    db.add(new_event)
    db.commit()

    return new_event


@app.put('/get-event/{name}')
async def update_event(name:str,event:Event):
    event_to_update = db.query(models.Event).filter(models.Event.name==name).first()
    event_to_update.name = event.name,
    event_to_update.description = event.description,
    event_to_update.date = event.date,
    event_to_update.location= event.location,
    event_to_update.category = event.category,
    event_to_update.sponsors = event.sponsors

    db.commit()
    return event_to_update

@app.delete('/get-event/{name}')
async def delete_event(name:str):
    delete_it = db.query(models.Event).filter(models.Event.name==name).first()

    db.delete(delete_it)
    db.commit()
    return delete_it


