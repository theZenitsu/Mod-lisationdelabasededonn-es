from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, DateTime, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

# Table for many-to-many relationship
AnnonceEquipement = Table(
    'annonce_equipement', Base.metadata,
    Column('annonce_id', ForeignKey('annonce.id'), primary_key=True),
    Column('equipement_id', ForeignKey('equipement.id'), primary_key=True)
)

class Ville(Base):
    __tablename__ = 'ville'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    annonces = relationship('Annonce', back_populates='ville')

class Equipement(Base):
    __tablename__ = 'equipement'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    annonces = relationship('Annonce', secondary=AnnonceEquipement, back_populates='equipements')

class Annonce(Base):
    __tablename__ = 'annonce'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    price = Column(String, nullable=True)
    datetime = Column(DateTime, nullable=False)
    nb_rooms = Column(Integer, nullable=True)
    nb_baths = Column(Integer, nullable=True)
    surface_area = Column(Float, nullable=True)
    link = Column(String, nullable=False)
    city_id = Column(Integer, ForeignKey('ville.id'))
    ville = relationship('Ville', back_populates='annonces')
    equipements = relationship('Equipement', secondary=AnnonceEquipement, back_populates='annonces')
