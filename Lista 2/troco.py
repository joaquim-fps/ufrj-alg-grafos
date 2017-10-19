def get_change():
    while True:
        change = int(input())

        # Só aceita valores maiores que 0
        if change > 0:
            return change

def coins():
    import math
    
    change = get_change()

    coin_values = [1, 5, 10, 25, 50, 100]
    coin_values.reverse()
    
    coin_amount = {coin : 0 for coin in coin_values}

    for coin in coin_values:
            if change >= coin:
                coin_amount[coin] = math.floor(change / coin)
                change = change % coin

            if change == 0:
                break

    return coin_amount

# 5) Contra-exemplo para coin_values = [1, 15, 20] 
# change = 30
# coin_amount[20] = math.floor(30 / 20) = 1
# change = 30 % 20 = 10
# (10 < 15) -> coin_amount[15] = 0
# coin_amount[1] = math.floor(10 / 1) = 10
# change = 10 % 1 = 0
# coin_amount = {20: 1, 15: 0, 1: 10}
# Quando, na verdade, a solução ótima seria coin_amount = {20: 0, 15: 2, 1: 0}