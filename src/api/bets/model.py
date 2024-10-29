from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.db.database import Base
from src.api.allbets.model import AllBets



class BetModel(Base):
    __tablename__ = 'Bets'

    id = Column(Integer, primary_key=True)
    bet_datetime = Column(DateTime)
    market = Column(String)
    arb_or_value = Column(String)
    amount = Column(Float)
    koef = Column(Float)
    bk2_koef = Column(Float)
    pre_koef = Column(Float)
    acc_id = Column(Integer, ForeignKey("Accounts.id", ondelete='CASCADE'))
    account = relationship("AccountModel", back_populates="bets")
    arb_or_value_percent = Column(Float)
    balance = Column(Float)
    name = Column(String)


class AccountModel(Base):
    __tablename__ = 'Accounts'

    id = Column(Integer, primary_key=True)
    login = Column(String)
    bets = relationship("BetModel", back_populates="account")
    allbets = relationship("AllBets", back_populates="account")
