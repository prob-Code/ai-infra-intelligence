from config.database import engine
from models.metrics import Base


def create_tables():
    Base.metadata.create_all(bind=engine)