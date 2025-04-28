from typing import Optional
from pydantic import BaseModel

class ResultSchema(BaseModel):
    job_name: str
    company_name: str
    url: str
    expired:str
    email: str | None = None