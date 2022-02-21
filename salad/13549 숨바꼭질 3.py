# 13549 숨바꼭질 3

# 걷기 x -> x-1 or x+1 (1초 소요)
# 순간이동 x -> 2*x (0초 소요)

import sys
import heapq

INF = sys.maxsize

n, k = map(int, input().split())

# 흠.. distance 초기화를 어케하나
# 최대 노드개수로 초기화 
d = [INF] * 100001
queue = []

def dijkstra(n, k):
    d[n] = 0    # 시작 값을 0으로 초기화
    heapq.heappush(queue, [d[n], n])

    while queue:
        cur_d, cur_dest = heapq.heappop(queue)
        
        if d[cur_dest] < cur_d:
            continue
        if cur_dest == k:
            return
        
        for i in range(3):
            if i == 0:
                next_dest = int(cur_dest)-1
                next_d = 1
            elif i == 1:
                next_dest = int(cur_dest)+1
                next_d = 1
            else:
                next_dest = int(cur_dest) * 2
                next_d = 0
            
            if next_dest < 0 or next_dest > 100000:
                continue

            # 3개에 대해 탐색
            tmp_d = next_d + cur_d

            if d[next_dest] > tmp_d:
                d[next_dest] = tmp_d
                heapq.heappush(queue, [tmp_d, next_dest])

dijkstra(n, k)
print(d[k])