from app.database.db_handler import Base, engine
from app.models.coach import Coach
from app.models.athlete import Athlete
from app.models.session_detail import SessionDetail


def create_tables():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
