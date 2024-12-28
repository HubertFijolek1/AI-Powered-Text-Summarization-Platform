from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel

router = APIRouter(
    prefix="/summaries",
    tags=["summaries"]
)

class SummarizeRequest(BaseModel):
    text: str

@router.post("/")
def get_summary(request: SummarizeRequest):
    """
    Return a placeholder summary for the provided text.
    """
    # Placeholder logic
    summary = f"Summarized: {request.text[:50]}..."
    return {
        "original_text": request.text,
        "summary": summary
    }