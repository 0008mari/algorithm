# 10815 숫자 카드
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
tests = list(map(int, input().split()))

# 정렬해서 이진탐색 쓰자아...
cards = sorted(cards)
rst = 0

def bSearch(start, end, x):
    global rst
    if end < start:
        rst = -1
        return -1  # 실패
    
    mid = (end + start) // 2
    if x == cards[mid]:
        rst = mid
        return mid # 성공
    
    if x < cards[mid]:
        return bSearch(start, mid-1, x)
    else:
        return bSearch(mid+1, end,x)


for test in tests:
    bSearch(0, n-1, test)
    if rst == -1:
        print("0", end=' ')
    else:
        print("1", end= ' ')
        