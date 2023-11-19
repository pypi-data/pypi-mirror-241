import uvicorn
from sqlalchemy import create_engine, inspect
from .infrastructure.config import Config
from .init_db import init_database

def main():
    engine = create_engine(Config.DATABASE_URL)
    inspector = inspect(engine)

    if not inspector.get_table_names():
        print("init_database...")
        init_database()

    uvicorn.run("hTrackerIU.api.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()
