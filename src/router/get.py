from fastapi import APIRouter, HTTPException
from bson import ObjectId

from src.controller.extractor import extract_text_from_pdf
from src.controller.summarizer import summarize_resume
from src.router.router import resume_collection

router = APIRouter()


@router.get("/{resume_id}")
def get_resume(resume_id: str):
    try:
        resume = resume_collection.find_one({"_id": ObjectId(resume_id)})

        if not resume:
            raise HTTPException(status_code=404, detail="Resume not found")

        resume["_id"] = str(resume["_id"])
        return resume

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid resume ID")


@router.get("/")
def get_all_resumes():
    resumes = []

    for resume in resume_collection.find():
        resume["_id"] = str(resume["_id"])
        resumes.append(resume)

    return {
        "count": len(resumes),
        "data": resumes
    }
