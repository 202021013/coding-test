values = list(map(int,input().split()))
chess = [1,1,2,2,2,8]
answer = []

for i in range(6):
    a = chess[i]-values[i]
    answer.append(a)
print(*answer)