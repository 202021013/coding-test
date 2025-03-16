import sys
from collections import deque

# 1. BFS를 사용하여 최소 이동 횟수 계산 함수 생성하기
def death_game(N, K, moves):
    visited = [False] * N 
    queue = deque([(0, 0)])  # (현재 학생 번호, 이동 횟수)
    visited[0] = True
    
    while queue:
        current, count = queue.popleft()

        if current == K:  # 현재 학생이 K번 학생이면 이동 횟수 반환
            return count
        
        next_student = moves[current]
        if not visited[next_student]:
            visited[next_student] = True
            queue.append((next_student, count + 1))
            
    return -1  # K번 학생을 찾지 못한 경우

# 2. N,K 입력값을 받아서 그래프를 구성하기
N, K = map(int, sys.stdin.readline().split())
moves = [int(sys.stdin.readline().strip()) for _ in range(N)]

# 3. K번 학생을 찾으면 결과 출력하고 찾지 못한 경우 -1 출력하기
print(death_game(N, K, moves))
