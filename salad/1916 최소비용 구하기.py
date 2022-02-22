# 1916 최소비용 구하기
# (1) 다익스트라 이용하여 

import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = {}
for i in range(n+1):
    graph[i] = {}

for _ in range(m):
    start, end, cost = map(int, input().split())
    if end in graph[start].keys():
        # 이미 있으면 작은 경우에만 바꿈
        if graph[start][end] > cost:
            graph[start][end] = cost
    else:
        graph[start][end] = cost

start, end = map(int, input().split())

d = [INF] * (n+1)

def dijkstra(graph, start):
    d[start] = 0
    queue = []
    heapq.heappush(queue, [d[start], start])
    # 시작노드 탐색을 위해 초기화

    while queue:
        cur_d, cur_dest = heapq.heappop(queue)

        if d[cur_dest] < cur_d:
            continue

        for new_dest, new_d in graph[cur_dest].items():
            tmp_d = cur_d + new_d   # 거쳐가는 거리
            if tmp_d < d[new_dest]:
                # 현재 최단거리보다 거쳐가는게 더 가까움.
                d[new_dest] = tmp_d   # 최단거리 갱신
                heapq.heappush(queue, [tmp_d, new_dest])
    
    return d

dijkstra(graph, start)

print(d[end])