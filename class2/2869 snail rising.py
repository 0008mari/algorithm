# 달팽이는 올라가고 싶다


A, B, V = map(int, input().split())

V -= A
# 마지막날 간 거리는 무조건 뺌 !!!!

day = V // (A-B)

if ( V % (A-B) == 0):
    day += 1
else:
    day += 2

print(day)