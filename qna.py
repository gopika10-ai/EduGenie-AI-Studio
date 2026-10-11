"""Academic question-answering module."""
from ai_core import generate_text

async def answer_question(question: str) -> str:
    prompt = f"""
You are EduGenie, an educational assistant. Answer the student's question accurately and clearly.
Question: {question}

Start with a direct answer, then explain the reasoning in numbered steps if useful.
Mention uncertainty when relevant. Do not claim that generated information is guaranteed correct.
"""
    return await generate_text(prompt, temperature=0.25)
