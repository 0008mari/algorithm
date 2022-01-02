# 치킨배달
from sys import stdin
from itertools import combinations
from copy import deepcopy

input = stdin.readline


def chickenDistance(a, b):
    # a, b is 1*2 array-like type
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def getCityChickenDistance(houses, chickenDiners):
    chickenDistances = []
    for house in houses:
        tmp = []
        for chickenDiner in chickenDiners:
            tmp.append(chickenDistance(house, chickenDiner))
        chickenDistances.append(min(tmp))
    return sum(chickenDistances)

# main

n, m = map(int, input().split())
city = [[] for _ in range(n)]   # n*n
for i in range(n):
    city[i] = list(map(int, input().split()))

houses = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append([i, j])

chickenDiners = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chickenDiners.append([i, j])

chickenDinersNo = len(chickenDiners)
chickenDinersNoArray = list(range(chickenDinersNo))
selectionChickenDistance = []
for selection in combinations(chickenDinersNoArray, chickenDinersNo-m):
    # 셀렉션 만큼 제거된 새 치킨집 리스트
    newChickenDiners = deepcopy(chickenDiners)
    for index in sorted(selection, reverse=True):
        # index로 pop 할때 그냥하면 인덱스 바껴서 오류나서 큰거부터 pop 한다
        targetDiner = chickenDiners[index]
        newChickenDiners.pop(index)
    # 도시의 치킨 거리 계산
    selectionChickenDistance.append(getCityChickenDistance(houses, newChickenDiners))

# 조합 중 가장 작은 도시치킨거리
print(min(selectionChickenDistance))