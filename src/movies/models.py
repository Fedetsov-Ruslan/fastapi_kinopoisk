from sqlalchemy import Column, Integer, String, ForeignKey

from src.database import Base
from src.users.models import User


class UserMovies(Base):
    __tablename__ = "user_movies"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey(User.id))
    movie_id = Column(String)