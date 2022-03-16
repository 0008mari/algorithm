# 1697 숨바꼭질

from collections import deque

maxsize = 100000

# bfs
def bfs(start, end, visited):
    q = deque()
    q.append(start)

    while q:
        v = q.popleft()
        if v == end:
            return visited[v]
        for nx in (v-1, v+1, v*2):
            if 0 <= nx and nx <= maxsize:
                if not visited[nx]:
                    visited[nx] = visited[v] + 1
                    q.append(nx)



n, k = map(int, input().split())
visited = [0] * (maxsize+1)
print(bfs(n, k, visited))


