import os
from fastapi import FastAPI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER", "default_user")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "default_pass")
POSTGRES_DB = os.getenv("POSTGRES_DB", "default_db")

app = FastAPI(
    title="AI-Powered Text Summarization Platform",
    version="0.1.0",
    description="A platform to summarize text using AI models."
)


@app.get("/health")
def health_check():
    return {
        "status": "OK",
        "db_user": POSTGRES_USER,
        "db_name": POSTGRES_DB
    }
