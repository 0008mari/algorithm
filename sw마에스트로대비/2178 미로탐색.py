# 미로탐색 2178

from collections import deque

# visited에 카운트하면서가야겟다 

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for i in range(n):
    tmp = list(map(int, list(input())))
    graph[i] = tmp
# 0, 0부터 n-1,m-1까지 가는 길
# bfs
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# visited = [[False for _ in range(m)] for _ in range(n)]
# 미로문제 접근 - 그래프 자체에 +1 씩 해준다.

def bfs(graph, start, end):
    q = deque()
    q.append(start)

    while q:
        x, y = q.popleft()
        
        for d in range(4):
            xx = x + dx[d]
            yy = y + dy[d]
            if xx < 0 or xx >= n or yy < 0 or yy >= m:
                continue

            if graph[xx][yy] == 0:
                continue
            if graph[xx][yy] == 1:
                graph[xx][yy] = graph[x][y] + 1
                q.append((xx, yy))

    return graph[n-1][m-1]





print(bfs(graph, (0, 0), (n-1, m-1)))