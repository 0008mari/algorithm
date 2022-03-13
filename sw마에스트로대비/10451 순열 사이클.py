# 순열 사이클 
from collections import deque

# def permToGraph
def permToGraph(perm):
    graph = [0 for _ in range(len(perm)+1)]
    for i in range(len(perm)):
        graph[i+1] = perm[i]
    # print(graph)
    return graph

# def bfs
def bfs(graph, start, visited):
    # 근데 bfs의 의미가 없긴 함
    q = deque()
    q.append(start)
    # visited[start] = True

    while q:
        v = q.popleft()
        if not visited[v]:
            visited[v] = True
            q.append(graph[v])

# main

t = int(input())

for _ in range(t):
    n = int(input())
    perm = list(map(int, input().split()))
    visited = [False] * (n+1)
    count = 0
    # 입력 순열에서 graph로 변환
    # 단방향 
    graph = permToGraph(perm)
    for i in range(1, n+1):
        if not visited[i]:
            bfs(graph, i, visited)
            count += 1
    print(count)