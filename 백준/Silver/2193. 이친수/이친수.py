import sys

# 1.N 입력 받기
N = int(sys.stdin.readline())

# 2. DP 배열 정의 -> i자리 이친수의 개수를 저장할 배열
dp = [0] * (N + 1)

# 3. 초기값 설정
dp[1] = 1  # 1자리 이친수는 '1'
if N > 1:
    dp[2] = 1  # 2자리 이친수는 '10'

# 4. 점화식 적용
for i in range(3, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

# 5. 결과 출력
print(dp[N])