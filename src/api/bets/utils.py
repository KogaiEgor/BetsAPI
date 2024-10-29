from datetime import datetime


async def match_bets(read_bets: list, bets: list):
    result = []
    for bet in bets:
        t = datetime.fromisoformat(bet['time'])
        for read_bet in read_bets:
            t2 = datetime.fromisoformat(read_bet['time'])
            if abs((t - t2).total_seconds()) <= 10:
                result.append(read_bet)
                print("Bets matched")
                break

    return result


