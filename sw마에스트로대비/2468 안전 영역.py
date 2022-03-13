# 2468 안전 영역

from collections import deque
from sys import stdin

input = stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# copy
def copyAlter(graph, n, rain):
    new = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= rain:
                new[i][j] = 0
            else:
                new[i][j] = graph[i][j]
    return new


# bfs
def bfs(graph, i, j):
    # 시작위치 - i, j
    n = len(graph)

    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()
        for d in range(4):
            xx = x + dx[d]
            yy = y + dy[d]
            if xx < 0 or xx >= n or yy < 0 or yy >= n:
                continue
            if graph[xx][yy] > 0:
                graph[xx][yy] = 0
                q.append((xx, yy))




n = int(input())
graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, input().split()))


maxrain = max(max(graph))
counts = []
for rain in range(0, maxrain+1):
    count = 0
    graph_tmp = copyAlter(graph, n, rain)
    for i in range(n):
        for j in range(n):
            if graph_tmp[i][j] > 0:
                count += 1
                bfs(graph_tmp, i, j)
    counts.append(count)

print(max(counts))
    
