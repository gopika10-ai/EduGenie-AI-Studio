"""Shared Google Gemini client wrapper."""
import os
from functools import lru_cache
from google import genai
from google.genai import types

@lru_cache(maxsize=1)
def get_client():
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key or api_key == "paste_your_key_here":
        raise EnvironmentError(
            "Gemini API key is missing. Add GEMINI_API_KEY to your local .env file."
        )
    return genai.Client(api_key=api_key)

async def generate_text(prompt: str, temperature: float = 0.3) -> str:
    client = get_client()
    model = os.getenv("GEMINI_MODEL", "gemini-3.8-flash").strip()
    response = await client.aio.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=2500,
        ),
    )
    answer = (response.text or "").strip()
    if not answer:
        raise RuntimeError("The AI service returned an empty response.")
    return answer
