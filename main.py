
from typing import List
from fastapi import FastAPI,status,HTTPException
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

db=SessionLocal()


#To get event details

@app.get('/get-event',response_model=List[Event],status_code=200)
async def get_all_events():
    events = db.query(models.Event).all()

    return events

# To get events by name
@app.get('/get-event/{name}',response_model=Event,status_code=status.HTTP_200_OK)
async def get_by_name(name:str):
    byname = db.query(models.Event).filter(models.Event.name==name).first()
    return byname

#To get events by location
@app.get('/get-event/{name}/{location}',response_model=Event,status_code=status.HTTP_200_OK)
async def get_by_location(location:str):
    byplace = db.query(models.Event).filter(models.Event.location==location).first()
    return byplace

#To get events by category
@app.get('/get-event/{name}/{location}/{category}',response_model=Event,status_code=status.HTTP_200_OK)
async def get_by_category(category: str):
    bycat = db.query(models.Event).filter(models.Event.category == category).first()
    return bycat

#To create an event
@app.post('/get-event/',response_model=Event,status_code=status.HTTP_201_CREATED)
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

#To update an event
@app.put('/get-event/{name}',response_model=Event,status_code=status.HTTP_200_OK)
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

#To delete an event
@app.delete('/get-event/{name}')
async def delete_event(name:str):
    delete_it = db.query(models.Event).filter(models.Event.name==name).first()

    db.delete(delete_it)
    db.commit()
    return delete_it


