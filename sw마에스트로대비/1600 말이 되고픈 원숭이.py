# 1600 말이 되고픈 원숭이

from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

d1 = [-2, -1, 1, 2, 2, 1, -1, -2]
d2 = [1, 2, 2, 1, -1, -2, -2, -1]

k = int(input())
w, h = map(int, input().split())
graph = [[] for _ in range(h)]
for i in range(h):
    graph[i] = list(map(int, input().split()))

# 함수정의
# def getMove(d1, d2, x, y):
#     # d1, d2에 따라 8방향 이동.
#     if d1 == 0 or d1 == 1:
#         # 좌우로 2칸 이동 + 상하로 1칸 이동
#         a = x + 2*dx[d1]
#         b = y + d2
#     else:
#         a = x + d2
#         b = y + 2*dy[d1]
#     return (a, b)


def isValid(x, y):
    if x<0 or x>=h or y<0 or y>=w:
        return False
    else:
        return True


def bfs(graph, k):
    # 0, 0에서 h,w 까지
    # return: 최소횟수
    left = k

    q = deque()
    q.append((0, 0, k))
    visited = [[[0 for _ in range(31)] for _ in range(w)] for _ in range(h)]

    while q:
        x, y, z = q.popleft()
        if x == h-1 and y == w-1:
            return visited[x][y][z]
        for d in range(4):
            xx = x + dx[d]
            yy = y + dy[d]
            if isValid(xx, yy):
                if graph[xx][yy] != 1 and visited[xx][yy][z] == 0:
                    q.append((xx, yy, z))
                    visited[xx][yy][z] = visited[x][y][z] + 1
        if z > 0:
            for d in range(8):
                xx = x + d1[d]
                yy = y + d2[d]
                if isValid(xx, yy):
                    if graph[xx][yy] != 1 and visited[xx][yy][z-1] == 0:
                        q.append((xx, yy, z-1))
                        visited[xx][yy][z-1] = visited[x][y][z] + 1
        
    return -1


print(bfs(graph, k))
