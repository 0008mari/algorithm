# 1764 듣보잡
# 교집합 구하기.

set1 = set()
set2 = set()

N, M = map(int, input().split())
for i in range(N):
    str = input()
    set1.add(str)
for i in range(M):
    str = input()
    set2.add(str)

dbj = set1 & set2

dbj = sorted(dbj)

print(len(dbj))
for name in dbj:
    print(name)