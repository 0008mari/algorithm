N, M = map(int, input().split())
weights = list(map(int, input().split()))
# 공 번호는 인덱스 + 1


count = 0
# 브루트포스 시도해봄 일단 ...
for i in range(0, N):
    for j in range(i+1, N):
        if weights[i] != weights[j]:
            count += 1

print(count)

