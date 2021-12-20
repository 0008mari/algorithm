import sys
input = sys.stdin.readline

count = 0

N, K = map(int, input().split())

# 최대한 많이 나누고, K보다 작을 때 1 빼기

# 많이 나누기
while N >= K:
    while N%K != 0:
        N -= 1
        count += 1
    N //= K
    count += 1

while N > 1:
    N -= 1
    count += 1

print(count)
