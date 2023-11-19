import os
from pathlib import Path

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from .routes import router

environment = os.getenv("ENV", "prod")

app = FastAPI()

if environment != "prod":
    origins = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(router, prefix="/api")

BASE_DIR = Path(__file__).resolve().parent.parent
static_files_path = BASE_DIR / "static" / "static"

if environment == "prod":
    app.mount("/static", StaticFiles(directory=str(static_files_path)), name="static")
    static_index_path = BASE_DIR / "static" / "index.html"

    @app.get("/{full_path:path}", response_class=HTMLResponse)
    async def catch_all(request: Request):
        if not request.url.path.startswith("/api"):
            return static_index_path.read_text()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
