# 백준 빙고
# https://www.acmicpc.net/problem/2578

import sys

# 3. 가로, 세로, 대각선 빙고를 처리하는 함수 만들기
def bingo():
    bingo_count = 0

    # 가로, 세로
    for i in range(5):
        if sum(board[i]) == 0:
            bingo_count += 1
        if sum(board[j][i] for j in range(5)) == 0:
            bingo_count += 1

    # 대각선
    if sum(board[i][i] for i in range(5)) == 0: 
        bingo_count += 1
    if sum(board[i][4 - i] for i in range(5)) == 0:
        bingo_count += 1

    return bingo_count


# 1. 빙고판 입력받기
board = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]

# 숫자 위치를 빠르게 찾기 위한 딕셔너리 추가
num_location = {}
for i in range(5):
    for j in range(5):
        num_location[board[i][j]] = (i, j)

# 2. 사회자가 부르는 숫자 입력 후 처리하기
count = 0
for _ in range(5):
    nums = list(map(int, sys.stdin.readline().split()))
    for num in nums:
        count += 1
        if num in num_location:
            x, y = num_location[num]
            board[x][y] = 0  # 숫자를 0으로 표시
        # 4. 빙고 3줄 이상이면 출력 후 종료
        if bingo() >= 3:
            print(count)
            exit()
