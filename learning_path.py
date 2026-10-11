"""Personalized learning path generation."""
from ai_core import generate_text

async def build_learning_path(topic: str) -> str:
    prompt = f"""
Design a practical learning path for a student who wants to learn: {topic}

Organize it into Beginner, Intermediate, and Advanced stages.
For each stage include:
- Learning goals
- Ordered topics to study
- A small hands-on activity
- A checkpoint to assess understanding
Finish with a suggested 4-week schedule and types of resources to look for.
Do not invent specific URLs. Keep the plan realistic for a beginner.
"""
    return await generate_text(prompt, temperature=0.5)
