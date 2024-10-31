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
    parsed_bet = relationship("ParsedBetModel", back_populates="bets", uselist=False)
    arb_or_value_percent = Column(Float)
    balance = Column(Float)
    name = Column(String)


class ParsedBetModel(Base):
    __tablename__ = 'ParsedBets'

    id = Column(Integer, primary_key=True)
    market = Column(String)
    odd = Column(Float)
    stake = Column(Float)
    amount_return = Column(Float)
    bets = relationship("BetModel", back_populates="parsed_bet", uselist=False, passive_deletes=True)
    account = relationship("AccountModel", back_populates="parsed_bets", passive_deletes=True)
    acc_id = Column(Integer, ForeignKey("Accounts.id", ondelete='CASCADE'), nullable=True)
    bet_id = Column(Integer, ForeignKey("Bets.id", ondelete='CASCADE'), nullable=True)


class AccountModel(Base):
    __tablename__ = 'Accounts'

    id = Column(Integer, primary_key=True)
    login = Column(String)
    bets = relationship("BetModel", back_populates="account")
    allbets = relationship("AllBets", back_populates="account")
    parsed_bets = relationship("ParsedBetModel", back_populates="account")




