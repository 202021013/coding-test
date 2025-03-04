import sys

N = int(sys.stdin.readline().strip())

mem_list = []
for _ in range(N):
    age, name = sys.stdin.readline().split()
    mem_list.append((int(age), name))

for mem in sorted(mem_list, key = lambda x: x[0]):
    print(mem[0],mem[1])