from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import logging

from ..import database,schemas,models,utils,oauth2


logger = logging.getLogger(__name__)

router = APIRouter(tags=["Authentication"])


@router.post("/login",response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    logger.info(f"Login request received: {user_credentials.username}")
    
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    logger.info(f"User found: {user}")

    if not user:
        logger.warning("Invalid credentials: User not found")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid credentials")

    if not utils.verify(user_credentials.password,user.password):
        logger.warning("Invalid credentials: Password mismatch")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid credentials")

    access_token = oauth2.create_access_token(data = {"user_id":user.id})
    logger.info("Login successful")
    return{"access_token" : access_token,"token_type": "bearer"}
