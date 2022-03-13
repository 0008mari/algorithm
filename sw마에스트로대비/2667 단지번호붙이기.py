# 2667 단지번호붙이기

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(graph, i, j):
    # 시작점 i, j
    # 몇칸이어져있는지 세서 리턴
    count = 0
    stack = []
    stack.append((i, j))
    n = len(graph)
    while stack:
        x, y = stack.pop()
        for d in range(4):
            xx = x + dx[d]
            yy = y + dy[d]
            if xx < 0 or xx >= n or yy < 0 or yy >= n:
                continue
            if graph[xx][yy] == 1:
                count += 1
                graph[xx][yy] = 0
                stack.append((xx, yy))
    if count == 0:
        count = 1
    return count


n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, list(input())))

house = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append(dfs(graph, i, j))

print(len(house))
for i in sorted(house):
    print(i)
