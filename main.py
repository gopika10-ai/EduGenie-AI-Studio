"""EduGenie: FastAPI entry point for an AI-powered learning workspace."""

from pathlib import Path
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from explanation_module import explain_concept
from qna import answer_question
from quiz_module import create_quiz
from summary_module import summarize_text
from learning_path import build_learning_path


# Resolve paths relative to this file so the app works
# even when started from a different working directory.
BASE_DIR = Path(__file__).resolve().parent

# Load environment variables from EduGenie_Original/.env
load_dotenv(BASE_DIR / ".env")

# Configure templates and static files.
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application startup and shutdown lifecycle."""
    yield


app = FastAPI(
    title="EduGenie Learning Studio",
    description=(
        "An AI-powered learning assistant for explanations, "
        "questions and answers, quizzes, summaries, and study plans."
    ),
    version="2.0.1",
    lifespan=lifespan,
)

# Serve CSS and other static assets.
app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static",
)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Render the EduGenie homepage."""
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={},
    )


@app.get("/health")
async def health():
    """Check whether the application is running."""
    return {
        "status": "ok",
        "app": "EduGenie Learning Studio",
    }


@app.post("/qa")
async def qa(topic: str = Form(...)):
    """Answer a learner's question."""
    return await run_feature(answer_question, topic)


@app.post("/explain")
async def explain(topic: str = Form(...)):
    """Explain a concept in learner-friendly language."""
    return await run_feature(explain_concept, topic)


@app.post("/quiz")
async def quiz(topic: str = Form(...)):
    """Generate a quiz about a topic."""
    return await run_feature(create_quiz, topic)


@app.post("/summarize")
async def summarize(topic: str = Form(...)):
    """Summarize the supplied text or topic."""
    return await run_feature(summarize_text, topic)


@app.post("/learn/recommendations")
async def recommendations(topic: str = Form(...)):
    """Build a personalized learning path."""
    return await run_feature(build_learning_path, topic)


async def run_feature(handler, user_text: str):
    """Validate input and safely run an AI feature."""

    cleaned = (user_text or "").strip()

    if len(cleaned) < 3:
        return JSONResponse(
            {"error": "Please enter at least 3 characters."},
            status_code=422,
        )

    if len(cleaned) > 12000:
        return JSONResponse(
            {"error": "Please keep your input under 12,000 characters."},
            status_code=413,
        )

    try:
        result = await handler(cleaned)
        return {"result": result}

    except EnvironmentError as exc:
        # For example, the Gemini API key is missing.
        return JSONResponse(
            {"error": str(exc)},
            status_code=503,
        )

    except Exception:
        # Keep internal details and credentials out of browser responses.
        return JSONResponse(
            {
                "error": (
                    "EduGenie could not complete that request. "
                    "Check the VS Code terminal, internet connection, "
                    "and Gemini API configuration, then try again."
                )
            },
            status_code=502,
        )
