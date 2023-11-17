import logging
from pathlib import Path

from fastapi import Depends, Request, FastAPI
from fastapi.staticfiles import StaticFiles

from dew_gwdata.webapp.handlers import api
from dew_gwdata.webapp.handlers import site

logger = logging.getLogger(__name__)

app = FastAPI(debug=True)

static_path = Path(__file__).parent / "static"

app.mount("/static", StaticFiles(directory=static_path), name="static")
app.include_router(api.router)
app.include_router(site.router)
