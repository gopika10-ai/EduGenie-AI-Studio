"""Concept explanation module with a beginner-first teaching prompt."""
from ai_core import generate_text

async def explain_concept(topic: str) -> str:
    prompt = f"""
You are EduGenie, a patient tutor. Explain the requested concept for a beginner.
Topic or question: {topic}

Use this structure:
1. Simple meaning
2. Step-by-step explanation
3. One practical example
4. Three key takeaways
Use clear language, define technical terms, and do not invent facts. If the topic is ambiguous, state your assumption.
"""
    return await generate_text(prompt, temperature=0.45)
