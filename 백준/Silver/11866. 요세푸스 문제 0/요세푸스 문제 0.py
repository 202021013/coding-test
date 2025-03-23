from collections import deque
import sys

# 1. N,K 입력 받기
N, K = map(int, sys.stdin.readline().split())

# 2. 큐 초기화
queue = deque(range(1, N + 1))
result = []

# 3. 요세푸스 순열 만들기
while queue:
    queue.rotate(-(K - 1))
    result.append(queue.popleft())  # K번째 요소 제거

# 4. 결과 출력
print("<" + ", ".join(map(str, result)) + ">")
