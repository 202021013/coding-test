X = int(input())

n = 1
while X > (n * (n + 1)) // 2:
    n += 1

prev_sum = (n * (n - 1)) // 2
index = X - prev_sum

if n % 2 == 1:
    numerator = n + 1 - index
    denominator = index
else:
    numerator = index
    denominator = n + 1 - index

print(f"{numerator}/{denominator}")