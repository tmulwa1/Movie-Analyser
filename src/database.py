from sqlalchemy import create_engine, Column, Integer, String, Float, Date, Text, engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

Base = declarative_base()
engine = create_engine('sqlite:///data/movies.db')
Session = sessionmaker(bind=engine)

class Movie(Base):
    __tablename__ = 'movies'
    
    id = Column(Integer, primary_key=True)
    tmdb_id = Column(Integer, nullable=False)
    title = Column(String(255), nullable=False)
    release_year = Column(String(4))
    genres = Column(String(255))
    director = Column(String(255))
    runtime = Column(Integer)
    poster_path = Column(String(255))
    vote_average = Column(Float)
    my_rating = Column(Float)
    notes = Column(Text)
    date_watched = Column(Date)

def initialise_db():
    os.makedirs('data', exist_ok=True)
    Base.metadata.create_all(engine)
    return engine

def get_session():
    return Session()