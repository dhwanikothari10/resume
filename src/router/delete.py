from fastapi import APIRouter, HTTPException
from bson import ObjectId

from src.controller.extractor import extract_text_from_pdf
from src.controller.summarizer import summarize_resume
from src.router.router import resume_collection

router = APIRouter()

@router.delete("/{resume_id}")
def delete_resume(resume_id: str):
    try:
        result = resume_collection.delete_one({"_id": ObjectId(resume_id)})

        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Resume not found")

        return {"message": "Resume deleted successfully"}

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid resume ID")
