import uvicorn
from pathlib import Path
from .infrastructure.config import Config
from .init_db import init_database

def main():
    db_path = Path(Config.DATABASE_URL.split("///")[-1])
    if not db_path.exists():
        print("init_database...")
        init_database()

    uvicorn.run("hTrackerIU.api.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()
