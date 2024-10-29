from datetime import datetime, timedelta


async def match_bets(read_bets: list, bets: list):
    print(len(read_bets))
    print(len(bets))
    result = []
    count = 0
    for bet in bets:
        t = bet.bet_datetime
        for read_bet in read_bets:
            t2 = datetime.fromisoformat(read_bet['time']) + timedelta(hours=2)
            if abs((t - t2).total_seconds()) <= 10:
                result.append(read_bet)
                print(t)
                print(t2)
                print("Bets matched")
                count += 1
                break
    print(count)
    return result

