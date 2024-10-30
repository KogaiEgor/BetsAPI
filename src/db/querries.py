from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.logger import logger
from src.api.bets.model import BetModel, AccountModel
from src.api.allbets.model import AllBets



async def create_new_bet(session: AsyncSession, bet_data: dict):
    logger.info("Starting creation of new bet")
    async with session.begin():
        acc_id = await _get_or_create_account(session, bet_data['login'])
        logger.debug(f"Account ID fetched or created: {acc_id}")
        new_bet = BetModel(
            bet_datetime=bet_data['bet_datetime'],
            market=bet_data['market'],
            arb_or_value=bet_data['arb_or_value'],
            amount=bet_data['amount'],
            koef=bet_data['koef'],
            bk2_koef=bet_data['bk2_koef'],
            pre_koef=bet_data['pre_koef'],
            acc_id=acc_id,
            arb_or_value_percent=bet_data['arb_or_value_percent'],
            balance=bet_data['balance'],
            name=bet_data['name']
        )

        session.add(new_bet)
        logger.debug("New bet added to session but not committed")

    logger.info("New bet created successfully")
    return new_bet


async def create_new_allbet(session: AsyncSession, bet_data: dict):
    logger.info("Starting creation of new allbet")
    async with session.begin():
        acc_id = await _get_or_create_account(session, bet_data['login'])
        logger.debug(f"Account ID fetched or created: {acc_id}")
        new_bet = AllBets(
            time=bet_data['time'],
            market=bet_data['market'],
            match_name=bet_data['match_name'],
            is_placed=bet_data['is_placed'],
            acc_id=acc_id,
            meta=bet_data['meta']
        )

        session.add(new_bet)
        logger.debug("New allbet added to session but not committed")

    logger.info("New allbet created successfully")
    return new_bet


async def _get_or_create_account(session: AsyncSession, login: str):
    logger.debug(f"Checking existence of account with login '{login}'")
    account = await session.execute(select(AccountModel).filter(AccountModel.login == login))
    account = account.scalar_one_or_none()

    if account:
        logger.debug(f"Account found: {account.id}")
        return account.id
    else:
        new_account = AccountModel(login=login)
        session.add(new_account)
        logger.debug(f"New account created with login '{login}'")

        return new_account.id


async def get_bets_per_acc(session: AsyncSession, acc_id: int):
    bets = await session.execute(select(BetModel).filter(BetModel.acc_id == acc_id))
    bets_list = bets.scalars().all()
    logger.info(f"Total bets found: {len(bets_list)} for account {acc_id}")

    return bets_list



