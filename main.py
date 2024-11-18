from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Ville, Annonce, Equipement

# Database connection
DATABASE_URL = "postgresql://postgres:    @localhost:5432/real_estate"

engine = create_engine(DATABASE_URL)

# Create tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Example: Insert a city
new_city = Ville(name="KENITRA")
session.add(new_city)
session.commit()

# Example: Query cities
cities = session.query(Ville).all()
for city in cities:
    print(city.name)
