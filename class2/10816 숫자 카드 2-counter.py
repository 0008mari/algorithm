# 10816 숫자 카드 2

from collections import Counter

N = int(input())
li = input().split()
M = int(input())
li2 = input().split()

counter = Counter(li)

for i in li2:
    print(counter[i], end=' ')

