from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine("postgresql://drxtvgxmxkicix:06decdbd37e6b6a1f78453059699d5ec0ef463e13917f59c4f3b7b7f7b181a7f@ec2-34-227-135-211.compute-1.amazonaws.com:5432/d5u95l156m8uvf",
                       echo = True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
