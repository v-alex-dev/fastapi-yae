# app/main.py
#
# Application entry point.
# This file creates the FastAPI instance, wires up the middleware,
# registers the routers, and manages the database connection lifecycle.

from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.config.settings import settings
from app.db.database import connect_to_db, disconnect_from_db
from app.middleware.logging_middleware import LoggingMiddleware
from app.routes import health_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code before "yield" runs on startup
    await connect_to_db()
    yield
    # Code after "yield" runs on shutdown
    await disconnect_from_db()


app = FastAPI(title=settings.app_name, lifespan=lifespan)

# Register middleware (order matters: this one wraps every request)
app.add_middleware(LoggingMiddleware)

# Register routers
app.include_router(health_routes.router)
