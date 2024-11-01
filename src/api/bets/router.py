from src.logger import logger
from typing import List
from fastapi import APIRouter, status, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from src.db.database import get_async_session
from src.db.querries import create_new_bet, get_bets_per_acc, _get_or_create_account, create_parsed_bets
from .schemas import BetSchema, ReadBetsRequest
from .utils import match_bets



router = APIRouter(
    prefix="/bets",
    tags=["Bets"]
)

@router.post("/add_bet/", status_code=status.HTTP_201_CREATED)
async def create_bet(bet_data: BetSchema, session: AsyncSession = Depends(get_async_session)):
    try:
        new_bet = await create_new_bet(session, bet_data.dict())
        return {
            "id": new_bet.id,
            "msg": "Bet successfully added to db"
        }
    except Exception as e:
        logger.error(f"Error creating bet: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Failed to create bet")


@router.get("get_accs_bet", status_code=status.HTTP_200_OK)
async def get_accs_bets(login: str, session: AsyncSession = Depends(get_async_session)):
    try:
        acc_id = await _get_or_create_account(session, login)
        bets = await get_bets_per_acc(session, acc_id)
        return {"read_bets": bets}
    except Exception as e:
        logger.error(f"Error creating bet: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to get bets for acc {login}")



@router.post("/read_bets/", status_code=status.HTTP_201_CREATED)
async def get_read_bets(request_data: ReadBetsRequest, session: AsyncSession = Depends(get_async_session)):
    try:
        if len(request_data.read_bets) == 0 or len(request_data.login) == 0:
            raise HTTPException(status_code=400, detail=f"Wrong data input")

        acc_id = await _get_or_create_account(session, request_data.login)
        bets = await get_bets_per_acc(session, acc_id)
        await match_bets(request_data.read_bets, bets, acc_id)
        await create_parsed_bets(session, request_data.read_bets)

        return {"msg": "Successfully saved parsed bets"}
    except Exception as e:
        logger.error(f"Error creating read bet", exc_info=True)
        raise HTTPException(status_code=400, detail=f"Bad request")
