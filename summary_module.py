"""Study-note summarization module."""
from ai_core import generate_text

async def summarize_text(text: str) -> str:
    prompt = f"""
Summarize the following learning material for revision.
Preserve the original meaning and important facts. Do not add facts that are absent.
Return:
- A short overview
- The main ideas as bullet points
- Important terms and their meanings, if any
- One-sentence revision takeaway

Material:
{text}
"""
    return await generate_text(prompt, temperature=0.25)
