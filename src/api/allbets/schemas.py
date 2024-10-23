from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class AllBetsSchema(BaseModel):
    id: Optional[int]
    time: Optional[datetime]
    market: Optional[str]
    match_name: Optional[str]
    is_placed: Optional[bool]
    login: Optional[str]
    meta: Optional[str]

    class Config:
        from_attributes = True
