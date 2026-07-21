from pydantic import BaseModel
from enum import Enum

class Priority(str, Enum):
    low = "Low"
    medium = "Medium"
    high = "High"
    critical = "Critical"

class TicketRequest(BaseModel):
    ticket_id: str
    subcategory: str
    priority: Priority
    description: str | None = None