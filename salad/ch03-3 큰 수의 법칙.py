# 큰 수의 법칙 

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
li = list(map(int, input().split()))

rst = 0
li = sorted(li, reverse=True)
k = K

while (M>0):
    if k>0:
        print(li[0])
        rst += li[0]
        k -= 1
    else:
        print(li[1])
        rst += li[1]
        k = K
    M-=1

print("--", rst)