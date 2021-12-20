# 그리디
# 숫자 카드 게임

import sys 
input = sys.stdin.readline

N, M = map(int, input().split())

ar = [[0 for j in range(M)] for i in range(N) ]

for i in range(N):
    ar[i] = list(map(int, input().split()))

max = min(ar[0])
for i in range(N):
    if max < min(ar[i]):
        rst = min(ar[i])
        max = min(ar[i])

print(rst)