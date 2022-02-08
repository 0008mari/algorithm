# 11052 카드 구매하기

n = int(input())
packs = [0] + list(map(int, input().split()))
# index 맞추려고 앞에 0 끼움
# pricePer = []
# for idx in range(0, len(packs)):
#     pricePer.append(packs[idx]/(idx+1))

# 무지성그리디 - 실패
# DP ? ㅠㅠ
dp = [0 for _ in range(n+1)]
dp[1] = packs[0]    # p1
for i in range(1, n+1):
   for k in range(1, i+1):
       dp[i] = max(dp[i], dp[i-k] + packs[k])
           
print(dp[i])