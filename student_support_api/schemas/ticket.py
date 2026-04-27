from pydantic import BaseModel
from typing import Literal

class TicketCreate(BaseModel):
    title: str
    description: str
    priority: Literal["Low", "Medium", "High"]

class TicketUpdate(BaseModel):
    status: Literal["Open", "In Progress", "Resolved"]

class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: str
    status: str
    user_id: int