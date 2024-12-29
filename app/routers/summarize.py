from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field


router = APIRouter(
    prefix="/summaries",
    tags=["summaries"]
)


def mock_summarizer(text: str) -> str:
    """
    Pretend to call a real AI model here.
    Return a truncated version of the text as a 'summary'.
    """
    if not text:
        return ""
    return text[:30] + "... (mock summary)"


class SummarizeRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=5,
        description="Text to summarize (min 5 characters)."
    )


@router.post("/")
def get_summary(request: SummarizeRequest):
    cleaned_text = request.text.strip()
    if len(cleaned_text) < 5:
        raise HTTPException(status_code=422, detail="Text must be at least 5 characters")

    summary = mock_summarizer(cleaned_text)
    return {
        "original_text": cleaned_text,
        "summary": summary
    }