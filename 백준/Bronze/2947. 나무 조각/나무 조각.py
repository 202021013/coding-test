import sys

N = list(map(int, sys.stdin.readline().split()))

while N != sorted(N):
    for i in range(4):
        if N[i] > N[i+1]:
            temp = N[i]
            N[i] = N[i+1]
            N[i+1] = temp
            print(*N)