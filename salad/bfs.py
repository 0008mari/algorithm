# bfs

from collections import deque

# bfs 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    visited[start] = True

    while queue:
        # 큐가 빌때까지 반복
        v = queue.popleft()
        print(v, end = ' ')
        # v와 연결된 미방문 노드 큐에 넣기
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 그래프는 2차원 리스트로 정보 표현, 인덱스 0번은 비워둠
graph = [[]]

visited = [False]*9

bfs(graph, 1, visited)