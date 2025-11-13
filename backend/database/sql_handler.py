from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

class DatabaseHandler:
    def __init__(self):
        db_url = os.getenv("DATABASE_URL", "sqlite:///data/app.db")
        if db_url.startswith("postgres://"):
            db_url = db_url.replace("postgres://", "postgresql://")
        self.engine = create_engine(db_url, pool_pre_ping=True)
        self.Session = sessionmaker(bind=self.engine)
        print("[Database] Connected to:", db_url)

    def create_tables(self):
        try:
            Base.metadata.create_all(self.engine)  # Új táblák létrehozása
            print("[Database] Tables created successfully.")
        except SQLAlchemyError as e:
            print("[Database ERROR]", e)

    def get_session(self):
        return self.Session()
