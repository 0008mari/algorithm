# 18870 μ’ν μμΆ

import sys
input = sys.stdin.readline

N = int(input())
tmp = map(int, input().rstrip().split())

X = list(tmp)
Xset = sorted(set(X))

rst = list()

dic = {value: index for index, value in enumerate(Xset)}

for elem in X:
    print(dic[elem], end= ' ')

