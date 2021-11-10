# 9375 패션왕 신해빈

import sys
input = sys.stdin.readline
from collections import Counter

case = int(input())
for i in range(case):
    n = int(input())
    list = []
    rst = 1
    for j in range(n):
        str = input().rstrip().split()
        list.append(str[1])     # 옷 종류만 넣는다
    ct = Counter(list)
    for key, value in ct.items():
        rst *= (value +1)
    rst -= 1        # 모두 안입은 경우 제외
    print(rst)
