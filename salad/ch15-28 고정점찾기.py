# 고정점 찾기
# 이진탐색 직접 구현 

def binarySearch(ar, start, end):
    # ar: list/ x: target/ start, end: idx
    if end < start:
        return -1  # fail
    mid = (end + start) // 2
    if ar[mid] == mid:
        return mid     
    elif ar[mid] > mid:
        return binarySearch(ar, start, mid-1)
    else:
        return binarySearch(ar, mid+1, end)
    


n = int(input())
nums = list(map(int, input().split()))


rst = binarySearch(nums, 0, n-1)
print(rst)