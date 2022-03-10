# DFS와 BFS

from collections import deque


# dfs, bfs 함수 호출 
# v - 시작노드 = start

# def dfs(graph, start):
#     visited = [False] * (n+1)
#     stack = [start]

#     visited[start] = True

#     # 스택으로 구현 - 왠지 순서가 거꾸로 나옴
#     while stack:
#         v = stack.pop()
#         print(v, end=' ')
#         for i in graph[v]:
#             if not visited[i]:
#                 stack.append(i)
#                 visited[i] = True
                

def dfs(graph, v):
    print(v, end=' ')
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            dfs(graph, w)


def bfs(graph, start):
    visited = [False] * (n+1)
    q = deque()

    q.append(start)
    visited[start] = True

    while q:
        v = q.popleft()
        print(v, end=' ')
        # v에 연관된 노드 append
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


# DFS, BFS 외워서 쓰기 참 어렵 습니다...

n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    # 무방향이라 양쪽에 추가.

# 작은노드부터 우선 방문임
for i in range(1, n+1):
    graph[i].sort()

visited = [False] * (n+1)
dfs(graph, v)
print()
bfs(graph, v)