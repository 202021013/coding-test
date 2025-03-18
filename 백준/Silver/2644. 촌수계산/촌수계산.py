from collections import deque
import sys

def find_relation(n, x, y, relations):
    # 1. 그래프 초기화
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []
    
    # 2. 무방향 그래프
    for a, b in relations:
        graph[a].append(b)
        graph[b].append(a)

    # 3. 최단 촌수 탐색
    queue = deque([(x, 0)])  # (현재 노드, 촌수)
    visited = set([x])  # 방문한 노드 저장

    while queue:
        current, count = queue.popleft()  # 현재 노드와 촌수 가져오기

        # 4. 목표 노드(y) 찾으면 촌수 반환
        if current == y:
            return count

        # 5. 현재 노드에서 이동할 수 있는 모든 노드 탐색
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, count + 1))

    return -1  # 촌수 관계 없음

n = int(sys.stdin.readline()) 
x, y = map(int, sys.stdin.readline().split()) 
m = int(sys.stdin.readline())
relations = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

# 결과 출력
print(find_relation(n, x, y, relations))