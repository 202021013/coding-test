import sys

# 1. 하나의 사이클을 찾고 방문 표시하는 함수 생성하기
def find_cycle(start, perm, visited):
    current = start
    while not visited[current]:  # 방문하지 않은 노드일 때만 계속 탐색
        visited[current] = True
        current = perm[current]

# 2. 전체 순열에서 사이클 개수를 찾는 함수 생성하기
def count_cycles(n, perm):
    visited = [False] * (n + 1)
    cycle_count = 0

    for i in range(1, n + 1):
        if not visited[i]:  # 방문하지 않은 숫자라면 새로운 사이클 시작
            find_cycle(i, perm, visited)
            cycle_count += 1

    return cycle_count

# 3. T , N 입력받기
T = int(sys.stdin.readline().strip())

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    perm = [0] + list(map(int, sys.stdin.readline().split()))  # 순열이 1부터 N까지의 정수를 사용
    
    # 4. 결과 출력하기
    print(count_cycles(N, perm))

