# ㅠㅠ - 2트
# 2206 벽 부수고 이동하기

from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())
ar = [[0] for _ in range(n)]

for i in range(n):
    ar[i] = list(map(int, list(input().rstrip())))


visited = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]
# 3rd elem: 0이면 부수기 가능
#           1이면 부수기 불가
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
# elem 1st, 2nd - 좌표
# 3rd - isBroken & 거리 동시에
#   0 - 미방문, 양수 - 방문, 거리

result = -1

def bfs():
    queue = deque([(0, 0, 0)])  
    visited[0][0][0] = 1

    while queue:
        cur = queue.popleft()
        isBroken = cur[2]
        if cur[0] == n-1 and cur[1] == m-1:
            result = visited[cur[0]][cur[1]][isBroken]
            return result    # 탐색 종료
        for d in range(4):
            xx = cur[0] + dx[d]
            yy = cur[1] + dy[d]
            if 0 <= xx and xx < n and 0<= yy and yy < m and visited[xx][yy][isBroken] == 0:
                if ar[xx][yy] == 0: # 전진 가능
                    queue.append((xx, yy, isBroken))
                    visited[xx][yy][isBroken] = visited[cur[0]][cur[1]][isBroken] + 1
                else:   # 전진 불가
                    if not isBroken:   # 벽부수기 가능
                        queue.append((xx, yy, 1))
                        visited[xx][yy][1] = visited[cur[0]][cur[1]][isBroken] + 1
                    # 벽부수기 불가 - 더이상 진행 안 됨, 처리 할 것 없음.
    return -1

print(bfs())