import webbrowser
from threading import Timer

import uvicorn
from sqlalchemy import create_engine, inspect

from .infrastructure.config import Config
from .init_db import init_database


def open_browser():
    webbrowser.open_new("http://localhost:8090")


def main():
    engine = create_engine(Config.DATABASE_URL)
    inspector = inspect(engine)

    if not inspector.get_table_names():
        print("init_database...")
        init_database()

    Timer(1, open_browser).start()

    uvicorn.run("hTrackerIU.api.main:app",
                host="0.0.0.0", port=8090, reload=True)


if __name__ == "__main__":
    main()
