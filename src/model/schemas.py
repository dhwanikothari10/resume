from pydantic import BaseModel
from typing import List


class ResumeSummary(BaseModel):
    summary: str
    skills:List[str]
