from datetime import datetime, timedelta

from src.logger import logger


async def match_bets(read_bets: list, bets: list):
    logger.info(f"Read {len(read_bets)}, found in db {len(bets)}")
    result = []
    count = 0
    logger.debug(f"Start matching bets")
    for bet in bets:
        t = bet.bet_datetime
        for read_bet in read_bets:
            t2 = datetime.fromisoformat(read_bet['time']) + timedelta(hours=2)
            if abs((t - t2).total_seconds()) <= 10:
                bet_id = bet.id
                read_bet['bet_id'] = bet_id
                result.append(read_bet)
                logger.debug("Bets matched")
                count += 1
                break
    logger.info(f"Total matched bets {count}/{len(bets)}")
    return result

