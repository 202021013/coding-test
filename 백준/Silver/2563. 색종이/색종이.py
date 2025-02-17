paper = [[0] * 100 for _ in range(100)]

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1         # 색종이 붙은 부분을 1로 표시

covered_area = sum(sum(row) for row in paper)

print(covered_area)