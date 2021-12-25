# 출처 https://gist.github.com/d36choi/43af4fa5df86c748462f5b8ee1f8e880#file-18405-py

from sys import stdin
from collections import deque

move = [[-1,0],[1,0],[0,-1],[0,1]]
N, K = map(int, stdin.readline().split())
board = [list(map(int,stdin.readline().split())) for _ in range(N)]
S, X, Y = map(int, stdin.readline().split())

q = []
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            q.append([board[i][j], i, j, 0])

q.sort()
q = deque(q)
X -= 1
Y -= 1  # index 는 0부터 시작하니까 

while q:
    virus, x, y, time = q.popleft()
    if time == S:
        break
    else:
        for [dx, dy] in move:
            if 0 <= x + dx < N and 0 <= y + dy < N and board[x + dx][y + dy] == 0:
                board[x + dx][y + dy] = virus
                q.append([virus, x + dx, y + dy, time + 1])

print(board[X][Y])