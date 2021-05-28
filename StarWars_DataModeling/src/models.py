import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    birth_day = Column(String(10), nullable=False)
    eye_color = Column(String(10), nullable=False)
    gender = Column(String(10), nullable=False)
    hair_color = Column(String(10), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    skin_color = Column(String(10), nullable=False)
    homeworld = Column(String(50), nullable=False )
    species = Column(String(50), nullable=False )

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship (Characters)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(10), nullable=False)
    terrain = Column(String(10), nullable=False)
    surface_water = Column(String(1), nullable=False)
    residents = Column(String(10), nullable=False)

class Starships(Base):
    __tablename__ = 'starships'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship (Planets)
    name = Column(String(100), nullable=False)
    model = Column(String(50), nullable=False)
    starships_class = Column(String(50), nullable=False)
    manufacturer = Column(String(100), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    max_atmosphering_speed = Column(String(10), nullable=False)
    hiperdrive_rating = Column(String(5), nullable=False)
    MGLT = Column(String(25), nullable=False)
    cargo_capacity = Column(String(25), nullable=False)
    consumables = Column(String(15), nullable=False)

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(10), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users)
    idCharacters = Column(String(10), nullable=False)
    idPlanets = Column(String(10), nullable=False)
    idStarships = Column(String(10), nullable=False)

    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
