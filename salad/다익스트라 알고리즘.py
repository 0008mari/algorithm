# 다익스트라 알고리즘
# 출처: https://justkode.kr/algorithm/python-dijkstra

import sys
import heapq

INF = sys.maxint

graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

n = 7   # 노드의 개수
d = [INF * n]



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
                heapq.heappush(queue, [d, new_dest])
    
    return d


