# 16234 인구 이동
from collections import deque

N, L, R = map(int, input().split())
A = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    A[i] = list(map(int, input().split()))

day = 0
graph = dict()


def check(tmpUnion, input, x, y):
    if input >= L and input <= R:
        tmpUnion.append((x, y))


def border(i, j):
    tmpUnion = []
    # 인접한 4방향 체크해서 연합 만들기
    if i-1 >= 0:
        top = abs(A[i-1][j]-A[i][j])
        check(tmpUnion, top, i-1, j)
    if i+1 < N:
        bottom = abs(A[i+1][j]-A[i][j])
        check(tmpUnion, bottom, i+1, j)
    if j-1 >= 0:
        left = abs(A[i][j-1]-A[i][j])
        check(tmpUnion, left, i, j-1)
    if j+1 < N:
        right = abs(A[i][j+1]-A[i][j])
        check(tmpUnion, right, i, j+1)

    if tmpUnion:
        # 원소 있으면
        graph[(i, j)] = tmpUnion


def bfs(start):
    visited = []
    queue = deque()
    queue.append(start)

    while queue:
        v = queue.popleft()
        if v not in visited:
            visited.append(v)
            queue.extend(graph[v])

    return visited

while(True):
    # 인접리스트 생성
    for i in range(N):
        for j in range(N):
            border(i, j)
    
    if not graph:
        break

    # 인구이동
    while graph:
        movement = bfs(list(graph.keys())[0])
        sum = 0
        # 연합 인구수 조정
        for move in movement:
            sum += A[move[0]][move[1]]
        result = int(sum/len(movement))
        for move in movement:
            A[move[0]][move[1]] = result
            del(graph[move]) # 연합 해체
    day += 1

print(day)


