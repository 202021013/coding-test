import sys

# 1. N 입력받기
N = int(sys.stdin.readline().strip())

count = [0] * (N + 1)  # 연산 횟수 저장

# 2. 1이 될때까지 1,2,3 연산 처리하기
for i in range(2, N + 1):
    count[i] = count[i - 1] + 1  # 3번 연산

    if i % 2 == 0:  # 2번 연산
        count[i] = min(count[i], count[i // 2] + 1)
    
    if i % 3 == 0:  # 1번 연산
        count[i] = min(count[i], count[i // 3] + 1)

# 3. 연산횟수 출력하기
print(count[N])