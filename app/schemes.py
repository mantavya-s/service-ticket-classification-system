from pydantic import BaseModel

class TicketRequest(BaseModel):
    subcategory: str
    description: str | None = None

class TicketResponse(BaseModel):
    prediction: str
    confidence: float