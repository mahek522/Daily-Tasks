from fastapi import FastAPI
from routes import auth, tickets

app = FastAPI(title="Student Support Ticket API")

app.include_router(auth.router)
app.include_router(tickets.router)