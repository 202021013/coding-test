N, B = map(int, input().split())

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""

while N > 0:
    r = N % B
    result = digits[r] + result
    N = N // B

print(result)