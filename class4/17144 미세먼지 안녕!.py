# 17144 미세먼지 안녕!

from sys import stdin
input = stdin.readline


def findDust(room, r, c):
    dustlist = []
    # 원소: (먼지양, col, row)
    for col in range(r):
        for row in range(c):
            if room[col][row] > 0:
                dustlist.append((room[col][row], col, row))
    return dustlist


def isValidLoc(x, y, r, c, room):
    if x >= 0 and x < r and y >= 0 and y < c:
        if room[x][y]!=-1:
            return True
    return False

r, c, t = map(int, input().split())
room = [[0] for _ in range(r)]
for col in range(r):
    room[col] = list(map(int, input().split()))
# 문제는 1,1 부터인데 이거는 0,0 부터임 (별상관x)

# 공기청정기 정보 저장
purifierLoc = []
for col in range(r):
    if room[col][0] == -1:
        purifierLoc.append((col, 0))

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

for time in range(t):
    # 1. 확산
    # 미세먼지 위치와 정보 저장
    dustlist = findDust(room, r, c)
    # 확산 레이어 생성
    effect = [[0 for _ in range(c)] for _ in range(r)]
    
    # 모든 먼지에 대해 4방향 확산
    for dust in dustlist:
        dustValue, x, y = dust[0], dust[1], dust[2]
        for d in range(4):
            xx = x + dx[d]
            yy = y + dy[d]
            if not isValidLoc(xx, yy, r, c, room):
                continue    # 막힌 곳은 확산 진행 x
            effect[xx][yy] += room[x][y] // 5
            effect[x][y] -= room[x][y] // 5
    # effect 덧씌우기 
    for col in range(r):
        for row in range(c):
            room[col][row] += effect[col][row]
    
    # 2. 공기청정기 작동
    p1 = purifierLoc[0][0]
    p2 = purifierLoc[1][0]
    # (8)
    for i in range(p2+1, r-1):
        room[i][0] = room[i+1][0]
    # (7)
    for i in range(p1-1, 0, -1):
        room[i][0] = room[i-1][0]
    # (6)
    for i in range(0, c-1):
        room[r-1][i] = room[r-1][i+1]
    # (5)
    for i in range(0, c-1):
        room[0][i] = room[0][i+1]
    # (4)
    for i in range(r-1, p1, -1):
        room[i][c-1] = room[i-1][c-1]
    # (3)
    for i in range(0, purifierLoc[0][0]):
        room[i][c-1] = room[i+1][c-1]    
    # (2)
    for i in range(c-1, 1, -1):
        room[p2][i] = room[p2][i-1]
    # (1)
    for i in range(c-1, 1, -1):
        room[p1][i] = room[p1][i-1]
    room[p1][1] = 0
    room[p2][1] = 0
    
        
rst = 0
for col in range(r):
    for row in range(c):
        rst += room[col][row]

print(rst+2)    #공청기정보-1