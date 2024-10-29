import logging
from fastapi import APIRouter, status, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from src.db.database import get_async_session
from src.db.querries import create_new_bet, get_bets_per_acc
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


@router.get("get_accs_bet", status_code=status.HTTP_200_OK)
async def get_accs_bets(login: str, session: AsyncSession = Depends(get_async_session)):
    try:
        bets = await get_bets_per_acc(session, login)
        print(bets)
        return {"read_bets": bets}
    except Exception as e:
        logging.error(f"Error creating bet: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to get bets for acc {login}")



