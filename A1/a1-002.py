x = int(input())
coins = [10, 5, 2, 1]

while x > 0:
    for coin in coins:
        count = 0
        if x >= coin:
            count = x//coin
            x -= count * coin
        print(f"{coin} = {count}")