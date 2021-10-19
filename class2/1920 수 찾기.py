# 1920: 수 찾기

def binarySearch(ar, x, start, end):
    # input: sorted array ar, key x
    # start = 0, end = len(ar)-1
    # output: index of x (if not exist, -1)
    
    if (start > end):
        return -1

    mid = (start+end)//2

    if (ar[mid] == x):
        return mid
    elif ar[mid] < x:
        start = mid+1
    elif ar[mid] > x:
        end = mid-1

    return binarySearch(ar, x, start, end)

# main

A = []

N = int(input())
A = (list)(map(int, input().split()))

M = int(input())
check = (list)(map(int, input().split()))

# sort A
A = sorted(A)

for i in range(len(check)):
    r = binarySearch(A, check[i], 0, len(A)-1)
    
    if r < 0:
        print("0")
    else:
        print("1")
