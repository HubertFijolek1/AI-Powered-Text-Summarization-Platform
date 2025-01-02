import os
import openai
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

openai.api_key = OPENAI_API_KEY

def summarize_with_openai(text: str) -> str:
    """
    Summarizes the input text using OpenAI's API.
    """
    if not text:
        return ""
    try:
        response = openai.ChatCompletion.create(
            model=OPENAI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that summarizes text."
                },
                {
                    "role": "user",
                    "content": f"Summarize the following text:\n\n{text}"
                }
            ],
            max_tokens=100,  # Adjust as needed
            temperature=0.3,  # Adjust creativity
        )
        summary = response.choices[0].message["content"].strip()
        return summary
    except Exception as e:
        # Fallback or re-raise error
        return f"Error calling LLM: {str(e)}"