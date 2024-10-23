import logging
from fastapi import APIRouter, status, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from src.db.database import get_async_session
from src.db.querries import create_new_bet
from .schemas import BetSchema


logging.basicConfig(level=logging.INFO)
router = APIRouter(
    prefix="/bets",
    tags=["Bets"]
)

@router.post("/add_bet/", status_code=status.HTTP_201_CREATED)
async def create_bet(bet_data: BetSchema, session: AsyncSession = Depends(get_async_session)):
    try:
        new_bet = await create_new_bet(session, bet_data.dict())
        return {"id": new_bet.id}
    except Exception as e:
        logging.error(f"Error creating bet: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to create bet")
