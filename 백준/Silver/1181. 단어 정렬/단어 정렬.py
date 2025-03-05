import sys

N = int(sys.stdin.readline().strip())

words = set(sys.stdin.readline().strip() for _ in range(N))

for word in sorted(words, key = lambda x: (len(x), x)):
    print(word)