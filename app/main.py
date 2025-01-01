import logging
from app.core.logging_config import setup_logging
from fastapi import FastAPI
from dotenv import load_dotenv
import os
from app.routers import summarize

from app.routers import auth
from app.routers import health

# Load environment variables from .env file
load_dotenv()

# Configure logging at startup
setup_logging()
logger = logging.getLogger(__name__)

POSTGRES_USER = os.getenv("POSTGRES_USER", "default_user")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "default_pass")
POSTGRES_DB = os.getenv("POSTGRES_DB", "default_db")

app = FastAPI(
    title="AI-Powered Text Summarization Platform",
    version="0.1.0",
    description="A platform to summarize text using AI models."
)

app.include_router(health.router)
app.include_router(auth.router)
app.include_router(summarize.router)

@app.on_event("startup")
async def on_startup():
    logger.info("Application is starting up...")

@app.on_event("shutdown")
async def on_shutdown():
    logger.info("Application is shutting down...")
