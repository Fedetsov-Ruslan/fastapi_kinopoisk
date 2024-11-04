
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

from src.database import Base


class User(Base):  
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    pasword_hash = Column(String)