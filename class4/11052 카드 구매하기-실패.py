# 11052 카드 구매하기

n = int(input())
packs = list(map(int, input().split()))
pricePer = []
for idx in range(0, len(packs)):
    pricePer.append(packs[idx]/(idx+1))

# 무지성그리디 
left = n
rst = 0
while left:
    next = pricePer.index(max(pricePer[:left]))
    left -= next+1
    rst += packs[next]
    # print(pricePer[next])


print(rst)