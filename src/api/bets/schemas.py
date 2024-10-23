from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

from src.api.allbets.schemas import AllBetsSchema


class BetSchema(BaseModel):
    id: Optional[int]
    bet_datetime: Optional[datetime]
    market: Optional[str]
    arb_or_value: Optional[str]
    amount: Optional[float]
    koef: Optional[float]
    bk2_koef: Optional[float]
    pre_koef: Optional[float]
    login: Optional[str]
    arb_or_value_percent: Optional[float]
    balance: Optional[float]
    name: Optional[str]

    class Config:
        from_attributes = True


class AccountSchema(BaseModel):
    id: Optional[int]
    login: Optional[str]
    bets: Optional[List[BetSchema]]
    allbets: Optional[List[AllBetsSchema]]

    class Config:
        from_attributes = True

