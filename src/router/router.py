from fastapi import APIRouter, UploadFile, File, HTTPException,BackgroundTasks
from database.conn import db
from bson import ObjectId


from src.controller.extractor import extract_text_from_pdf
from src.controller.summarizer import summarize_resume


router = APIRouter()
resume_collection = db["resume_summaries"]

async def save_resume_summary(response:dict):
    if not response:
        return

    document = {
        "text": response.get("text"),
        "summary": response.get("summary")
    }

    resume_collection.insert_one(document)

@router.post("/upload")
async def upload_resume(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...)
    ):
        
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    try:
        resume_text = extract_text_from_pdf(file.file)

        if not resume_text:
            raise HTTPException(status_code=400, detail="Could not extract text from PDF")

        result = summarize_resume(resume_text)

        record = {"text":resume_text, "summary":result}

        background_tasks.add_task(save_resume_summary, record)
        return result
    


    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
