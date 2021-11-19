# 11279 최대 힙

# 와 ~ 파이썬에는 놀랍게도 heapq 라는 게 있다~

import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []

# Max Heap
for _ in range(N):
    x = int(input())
    if x!=0:
        heapq.heappush(heap, (-x))
    else:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)