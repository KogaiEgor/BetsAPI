from datetime import datetime, timedelta

from src.logger import logger


async def match_bets(read_bets: list, bets: list, acc_id: int):
    logger.info(f"Read {len(read_bets)}, found in db {len(bets)}")
    count = 0
    logger.debug(f"Start matching bets")
    for read_bet in read_bets:
        read_bet['acc_id'] = acc_id
        for bet in bets:
            t = bet.bet_datetime
            t2 = datetime.fromisoformat(read_bet['time']) + timedelta(hours=2)
            if abs((t - t2).total_seconds()) <= 7:
                read_bet['bet_id'] = bet.id
                logger.debug(f"{read_bet}")
                count += 1
                break
    logger.info(f"Total matched bets {count}/{len(bets)}")


