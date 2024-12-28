from fastapi import APIRouter
from pydantic import BaseModel


def mock_summarizer(text: str) -> str:
    """
    Pretend to call a real AI model here.
    Return a truncated version of the text as a 'summary'.
    """
    if not text:
        return ""
    return text[:30] + "... (mock summary)"


router = APIRouter(
    prefix="/summaries",
    tags=["summaries"]
)


class SummarizeRequest(BaseModel):
    text: str


@router.post("/")
def get_summary(request: SummarizeRequest):
    """
    Return a mock AI-based summary for the provided text.
    """
    summary = mock_summarizer(request.text)
    return {
        "original_text": request.text,
        "summary": summary
    }
