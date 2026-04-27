from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from utils.jwt_handler import decode_token
from utils.logger import logger

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        user = decode_token(token)
        return user
    except:
        raise HTTPException(status_code=401, detail="Invalid token")
    
from fastapi import APIRouter, Depends, HTTPException
from models.ticket import tickets_db
from schemas.ticket import TicketCreate, TicketUpdate

router = APIRouter()

ticket_id_counter = 1

@router.post("/tickets")
def create_ticket(ticket: TicketCreate, user=Depends(get_current_user)):
    global ticket_id_counter

    new_ticket = {
        "id": ticket_id_counter,
        "title": ticket.title,
        "description": ticket.description,
        "priority": ticket.priority,
        "status": "Open",
        "user_id": user["user_id"]
    }

    tickets_db.append(new_ticket)
    ticket_id_counter += 1
    
    logger.info("New ticket created")

    return {
        "success": True,
        "data": new_ticket,
        "message": "Ticket created successfully"
    }
    
@router.get("/tickets")
def get_tickets(user=Depends(get_current_user)):
    if user["role"] == "staff":
        return {"success": True, "data": tickets_db}

    user_tickets = [t for t in tickets_db if t["user_id"] == user["user_id"]]

    return {"success": True, "data": user_tickets}

@router.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: int, user=Depends(get_current_user)):
    for t in tickets_db:
        if t["id"] == ticket_id:
            return {"success": True, "data": t}

    raise HTTPException(status_code=404, detail="Ticket not found")

@router.put("/tickets/{ticket_id}")
def update_ticket(ticket_id: int, update: TicketUpdate, user=Depends(get_current_user)):
    
    if user["role"] != "staff":
        raise HTTPException(status_code=403, detail="Only staff can update")

    for t in tickets_db:
        if t["id"] == ticket_id:
            t["status"] = update.status

            return {
                "success": True,
                "data": t,
                "message": "Ticket updated"
            }
    logger.info("Ticket updated")
    
    raise HTTPException(status_code=404, detail="Ticket not found")