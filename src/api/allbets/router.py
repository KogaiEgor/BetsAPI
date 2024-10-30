import logging
from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.querries import create_new_allbet
from src.db.database import get_async_session
from src.api.allbets.schemas import AllBetsSchema


logging.basicConfig(level=logging.INFO)
router = APIRouter(
    prefix="/allbets",
    tags=["AllBets"]
)

@router.post("/add_allbets/", status_code=status.HTTP_201_CREATED)
async def create_allbets(bet_data: AllBetsSchema, session: AsyncSession = Depends(get_async_session)):
    try:
        allbet = await create_new_allbet(session=session, bet_data=bet_data.dict())
        return {
            "id": allbet.id,
            "msg": "Allbet succesfully added to db"
        }
    except Exception as e:
        logging.error(f"Error creating bet: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to create allbet")
