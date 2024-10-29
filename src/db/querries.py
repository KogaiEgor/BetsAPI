from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.api.bets.model import BetModel, AccountModel
from src.api.allbets.model import AllBets



async def create_new_bet(session: AsyncSession, bet_data: dict):
    async with session.begin():
        acc_id = await _get_or_create_account(session, bet_data['login'])
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

    return new_bet


async def create_new_allbet(session: AsyncSession, bet_data: dict):
    async with session.begin():
        acc_id = await _get_or_create_account(session, bet_data['login'])
        new_bet = AllBets(
            time=bet_data['time'],
            market=bet_data['market'],
            match_name=bet_data['match_name'],
            is_placed=bet_data['is_placed'],
            acc_id=acc_id,
            meta=bet_data['meta']
        )

        session.add(new_bet)

    return new_bet


async def _get_or_create_account(session: AsyncSession, login: str):
    account = await session.execute(select(AccountModel).filter(AccountModel.login == login))
    account = account.scalar_one_or_none()

    if account:
        return account.id
    else:
        new_account = AccountModel(login=login)
        session.add(new_account)

        return new_account.id


async def get_bets_per_acc(session: AsyncSession, login: str):
    acc_id = await _get_or_create_account(session, login)
    print(acc_id)

    bets = await session.execute(select(BetModel).filter(BetModel.acc_id == acc_id))
    return bets.scalars().all()



