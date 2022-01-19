# 병사 배치하기
# boj 18353

n = int(input())

ar = list(map(int, input().split()))
ar.reverse()

dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if ar[j] < ar[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))