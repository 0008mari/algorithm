# 11724 연결 요소의 개수
# readline 안 쓰면 시간초과임.
from sys import stdin
from collections import deque

input = stdin.readline

def dfs(graph, start, visited):
    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        v = q.popleft()
        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                q.append(w)



n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
visited = [False] * (n+1)

for i in range(1, n+1):
    if not visited[i]:
        count += 1
        dfs(graph, i, visited)

print(count)