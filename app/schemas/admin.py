from pydantic import BaseModel

class IssueKeyRequest(BaseModel):
    note: str
    