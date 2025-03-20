from collections import deque
import sys

def wedding():
    # 1. n,m 입력받고 인접 리스트로 그래프 생성하기
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())

    # 양방향 그래프 구축
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    # 2. BFS 탐색
    queue = deque([1])  # 상근이부터 시작
    visited = [False] * (n+1) # 방문여부
    visited[1] = True

    depth = {1: 0}  # 시작 노드의 깊이 저장
    invite_count = 0  # 초대할 친구 수

    while queue:
        person = queue.popleft()
        if depth[person] >= 2:  # 깊이가 2 이상이면 탐색 중지
            continue

        for friend in graph[person]:
            if not visited[friend]:
                visited[friend] = True
                depth[friend] = depth[person] + 1
                queue.append(friend)
                invite_count += 1
    # 3. 결과출력
    print(invite_count)
    
wedding()