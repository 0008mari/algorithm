# 기타 레슨

import sys
input = sys.stdin.readline

def getBluNo(ar, size):
    blu = [0] * len(ar)
    bluIndex = 0

    for i in ar:
        if blu[bluIndex] + i <= size:
            blu[bluIndex] += i
        else:
            bluIndex += 1
            blu[bluIndex] += i
    return bluIndex + 1     # idx+1
        

def binarySearch(ar, start, end, m):
    if end < start:
        return -1  # fail
    size = (end + start) // 2

    # 블루레이 담기
    no = getBluNo(ar, size)
  
    if no > m:
        return binarySearch(ar, size+1, end, m)
    else:
        global ans
        ans = min(ans, size)
        return binarySearch(ar, start, size-1, m)


n, m = map(int, input().split())
ar = list(map(int, input().split()))
ans = sys.maxsize

binarySearch(ar, max(ar), sum(ar), m)
print(ans)
