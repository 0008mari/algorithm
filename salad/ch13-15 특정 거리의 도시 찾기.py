# 18352 특정 거리의 도시 찾기

# bfs

from collections import deque
import sys
input = sys.stdin.readline

# bfs 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # visited[start] = True

    # 각 노드에 도달하는 거리 저장 
    distances = [-1]*(n+1)
    distances[start] = 0     # 시작 노드 거리 0

    while queue:
        # 큐가 빌때까지 반복
        v = queue.popleft()
        # v와 연결된 미방문 노드 큐에 넣기
        for i in graph[v]:
            if distances[i] == -1: #미방문이면
                distances[i] = distances[v] + 1
                queue.append(i)
                # visited[i] = True

    return distances

# 그래프는 2차원 리스트로 정보 표현, 인덱스 0번은 비워둠

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
# 엣지 정보
    a, b = map(int, input().split())
    graph[a].append(b)

distances = bfs(graph, x, visited)

for i in range(1, n+1):
    if distances[i] == k:
        print(i)
if k not in distances:
    print(-1)