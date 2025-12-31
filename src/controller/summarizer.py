import json
import ollama
from datetime import datetime

from utils.prompt import SYSTEM_PROMPT
from src.model.schemas import ResumeSummary

current_date = datetime.now().strftime("%d %B %Y")    


def summarize_resume(resume_text: str) -> dict:
    response = ollama.chat(
        model="gpt-oss:20b-cloud",  
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": resume_text}
        ]
    )

    return response["message"]["content"]