from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from src.db.database import Base


class AllBets(Base):
    __tablename__ = 'AllBets'
    id = Column(Integer, primary_key=True)
    time = Column(DateTime)
    market = Column(String)
    match_name = Column(String)
    is_placed = Column(Boolean)
    acc_id = Column(Integer, ForeignKey("Accounts.id", ondelete='CASCADE'))
    account = relationship("AccountModel", back_populates="allbets")
    meta = Column(String)
