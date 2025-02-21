def calculate_change(cents):
    coins = [25, 10, 5, 1]
    result = []
    
    for coin in coins:
        result.append(cents // coin)
        cents %= coin
    
    return result

t = int(input().strip())
for _ in range(t):
    cents = int(input().strip())
    print(*calculate_change(cents))
