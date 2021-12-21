n = int(input())
coins = map(int, input().split())

coins = sorted(coins, reverse=True)

m = 1   # 검사 대상이 되는 금액
left = 1

while(True):
    left = m
    for i in coins:
        if i > left:
            continue
        left -= i
        if left == 0:
            break  
    if left > 0:
        break
    m += 1
print(m)

# 설명 - 가장 큰 동전 금액부터 뺀다
# 다 뺐는데 남은게 있으면 그 금액이 답

# 답지도 보자 