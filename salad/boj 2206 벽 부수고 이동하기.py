# 2206 벽 부수고 이동하기

from collections import deque

n, m = map(int, input().split())
ar = [[0] for _ in range(n)]

for i in range(n):
    ar[i] = list(map(int, list(input())))

# 벽 위치 수집
walls = []
for i in range(n):
    for j in range(m):
        if ar[i][j] == 1:
            walls.append((i, j))
            # 튜플생성해서넣음

maxRoute = 2000
result = [maxRoute for _ in range(len(walls))]
# 벽 하나씩 부수면서 최단경로 찾음 
for wall in walls:
    count = 0
    # 벽 부수기
    ar[wall[0]][wall[1]] = 0

    # bfs 경로찾기
    visited = [[False for _ in range(m)] for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque([(0, 0, 1)])
    # 세번째 원소는 거리임 
    visited[0][0] = True
    while queue:
        cur = queue.popleft()
        if cur[0] == n-1 and cur[1] == m-1:
            result[count] = cur[2]
            # 최단거리 집어넣기
        # 탐색
        for d in range(4):
            xx = dx[d] + cur[0]
            yy = dy[d] + cur[1]
            if 0 <= xx < n and 0 <= yy < m and not visited[xx][yy]:
                if d == 3 and ar[xx][yy] == 1:
                    continue    # 전진불가
                if ar[xx][yy] == 0:
                    visited[xx][yy] = True
                    queue.append((xx, yy, cur[2]+1))

    # 벽 복구
    ar[wall[0]][wall[1]] = 1

if min(result) == 2000:
    print(-1)
else:
    print(min(result))