from fastapi import FastAPI

app = FastAPI(
    title="AI-Powered Text Summarization Platform",
    version="0.1.0",
    description="A platform to summarize text using AI models."
)

@app.get("/health")
def health_check():
    return {"status": "OK"}