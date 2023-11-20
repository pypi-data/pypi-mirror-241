import argparse
import sys
import os
import webbrowser
from threading import Timer

import uvicorn
from sqlalchemy import create_engine, inspect

from .infrastructure.config import Config
from .init_db import init_database

def open_browser(port):
    webbrowser.open_new(f"http://localhost:{port}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=None,
                        help="Port to run the server on")
    args = parser.parse_args()

    # Check if port is passed as an argument
    port = args.port

    # If not, fall back to environment variable, then to default value
    if port is None:
        port = int(os.getenv("PORT", 8095))

    engine = create_engine(Config.DATABASE_URL)
    inspector = inspect(engine)

    if not inspector.get_table_names():
        init_database()

    Timer(1, open_browser, args=(port,)).start()

    try:
        uvicorn.run("hTrackerIU.api.main:app", host="0.0.0.0", port=port, reload=True)
    except SystemExit as e:
        print(f"ERROR: Port {port} is already in use.")
        print("You can specify a different port by using the --port argument")

if __name__ == "__main__":
    main()
