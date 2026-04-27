from fastapi import APIRouter, HTTPException
from schemas.user import UserLogin
from models.user import users_db
from utils.jwt_handler import create_token
from utils.logger import logger

router = APIRouter()

@router.post("/login")
def login(user: UserLogin):
    for u in users_db:
        if u["username"] == user.username and u["password"] == user.password:
            token = create_token({"user_id": u["id"], "role": u["role"]})
            return {
                "success": True,
                "data": {"token": token},
                "message": "Login successful"
            }
    logger.info("User logged in successfully")
    
    
    raise HTTPException(status_code=401, detail="Invalid credentials")