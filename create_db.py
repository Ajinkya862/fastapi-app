from database import Base,engine
from models import Event

print("Creating Database")

Base.metadata.create_all(engine)