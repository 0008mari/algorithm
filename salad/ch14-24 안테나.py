# ch 14 정렬
# 안테나

from sys import stdin
input = stdin.readline

# 우앙~~ 대박... 
# 무지성 거리구하기 하면 안되는구나..

n = int(input())
houses = list(map(int, input().split()))

houses = sorted(houses)

print(houses[(len(houses)-1)//2])


# 집의 최댓값이 200,000인 만큼 브루트포스로 접근하면 안 된다~