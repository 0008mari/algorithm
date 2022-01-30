# 9465 스티커
from sys import stdin
import heapq
input = stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    arr = [[0] for _ in range(2)]
    for i in range(2):
        arr[i] = list(map(int, input().split()))
    
    # greedy
    result = 0

    # 값이 높은거부터 정렬 유지하며 위치정보 저장
    # 최대힙 - 기준은 default: 첫번째 원소 기준
    heap = []
    for col in range(2):
        for row in range(n):
            heapq.heappush(heap, (-1 * arr[col][row], col, row))
            # 최대힙을 위해 -1 곱해서 저장
    
    for i in range(2*n):
        value, col, row = heap[i][0], heap[i][1], heap[i][2]
        if arr[col][row] == 0:
            continue    # 못쓰는칸.
        else:
            result += value
            print(value)
            arr[col][row] = 0
            if col == 0:
                if row == 0:
                    arr[col+1][row] = 0
                    arr[col][row+1] = 0
                elif row == n-1:
                    arr[col][row-1] = 0
                    arr[col+1][row] = 0
                else:
                    arr[col+1][row] = 0
                    arr[col][row-1] = 0
                    arr[col][row+1] = 0
            else:   # col == 1
                if row == 0:
                    arr[col-1][row] = 0
                    arr[col][row+1] = 0
                elif row == n-1:
                    arr[col-1][row] = 0
                    arr[col][row-1] = 0
                else:
                    arr[col-1][row] = 0
                    arr[col][row-1] = 0
                    arr[col][row+1] = 0

    # result * -1 해야됨
    print(result * -1)
            
