"""Quiz generation with tolerant parsing and a safe plain-text fallback."""
import json
import re
from ai_core import generate_text

def clean_json_block(raw: str) -> str:
    text = raw.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text)
    start, end = text.find("["), text.rfind("]")
    if start >= 0 and end > start:
        return text[start:end + 1]
    return text

async def create_quiz(topic_or_passage: str):
    prompt = f"""
Create exactly 5 educational multiple-choice questions from this topic or passage:
{topic_or_passage}

Return ONLY a valid JSON array. Each object must have:
"question": string,
"options": an array of exactly 4 short strings,
"answer": the exact text of the correct option,
"explanation": a brief explanation.
Do not use Markdown fences. Ensure only one best answer per question.
"""
    raw = await generate_text(prompt, temperature=0.35)
    try:
        parsed = json.loads(clean_json_block(raw))
        if not isinstance(parsed, list) or not parsed:
            raise ValueError("Expected a non-empty JSON array.")
        valid = []
        for item in parsed[:5]:
            if not isinstance(item, dict):
                continue
            question = str(item.get("question", "")).strip()
            options = item.get("options", [])
            answer = str(item.get("answer", "")).strip()
            explanation = str(item.get("explanation", "")).strip()
            if question and isinstance(options, list) and len(options) == 4 and answer:
                valid.append({
                    "question": question,
                    "options": [str(option) for option in options],
                    "answer": answer,
                    "explanation": explanation,
                })
        if not valid:
            raise ValueError("No valid quiz questions were returned.")
        return valid
    except (json.JSONDecodeError, ValueError, TypeError):
        return {"format_note": "The model did not return valid quiz JSON. Here is its response to review.", "raw_response": raw}
