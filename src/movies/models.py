from sqlalchemy import Column, Integer, String, ForeignKey

from src.database import Base
from src.users.models import User
  
    
class Movies(Base):
    __tablename__ = "movies"
    
    kinopoisk_id = Column(String, primary_key=True)
    title = Column(String)
    year = Column(Integer)
    description = Column(String)
    poster = Column(String)
    rating = Column(Integer)
    rating_kinopoisk = Column(Integer)
    rating_imdb = Column(Integer)
    movie_length = Column(Integer)
    
    
class UserMovies(Base):
    __tablename__ = "user_movies"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey(User.id))
    movie_id = Column(String, ForeignKey(Movies.kinopoisk_id))
