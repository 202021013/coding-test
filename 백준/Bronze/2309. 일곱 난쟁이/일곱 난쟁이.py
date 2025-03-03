from itertools import combinations

height_list = [int(input()) for _ in range(9)]

for comb in combinations(height_list, 2):
    if sum(height_list)- sum(comb) == 100:
        height_list.remove(comb[0])
        height_list.remove(comb[1])

for height in sorted(height_list):
    print(height)