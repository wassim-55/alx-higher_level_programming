#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

mymetadata = MetaData()
Base = declarative_base(MetaData=mymetadata)

class State(Base):
    """
    class with id and name attributesof each state
    """
    __tablename__ = 'states'
    id = column(Integer, unique=True, nullable=False, primary_Key=True)
    name = column(String(128), nullable=False)
    cities = relationship("City", backref="states")
