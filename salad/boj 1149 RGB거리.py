# RGB 거리

N = int(input())
colorCost = [[0] for _ in range(N)]
for i in range(N):
    colorCost[i] = list(map(int, input().split()))

rstList = []

for i in range(1, N):
    colorCost[i][0] = min(colorCost[i-1][1], colorCost[i-1][2]) + colorCost[i][0]
    colorCost[i][1] = min(colorCost[i-1][0], colorCost[i-1][2]) + colorCost[i][1]
    colorCost[i][2] = min(colorCost[i-1][0], colorCost[i-1][1]) + colorCost[i][2]

print(min(colorCost[N-1]))