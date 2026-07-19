from pydantic import BaseModel

class TicketRequest(BaseModel):
    subcategory: str
    description: str | None = None

class TicketResponse(BaseModel):
    prediction: str
    confidence: float

class RetrieveRequest(BaseModel):
    text: str
    limit: int = 3