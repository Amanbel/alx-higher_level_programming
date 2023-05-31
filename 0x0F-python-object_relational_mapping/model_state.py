#!/usr/bin/python3
"""
Base modules
"""

from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """State Class"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
