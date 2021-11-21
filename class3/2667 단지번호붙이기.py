# 2667 단지번호붙이기

houseNo = []
complexNo = 0
houseCount = 0

# 이거 무슨? 그래프탐색? 그런거임 

def checkHouse(ar, i, j, N):
    global houseCount

    if ar[i][j] == 0:
        return
    else:
        houseCount += 1
        ar[i][j]=0

    if (i>0):
        if (ar[i-1][j] > 0):
            checkHouse(ar, i-1, j, N)
    if (i<N-1):
        if (ar[i+1][j] > 0):
            checkHouse(ar, i+1, j, N)
    if (j>0):
        if (ar[i][j-1] > 0):
            checkHouse(ar, i, j-1, N)
    if (j<N-1):
        if (ar[i][j+1] > 0):
            checkHouse(ar, i, j+1, N)


# main

N = int(input())
houseMap = [[0 for j in range(N)] for i in range(N)]

for i in range(N):
    tmp = input()
    for j in range(N):
        houseMap[i] = list(map(int, list(tmp)))


# object detection
for i in range(N):
    for j in range(N):
        if houseMap[i][j] == 0:
            continue
        else:
            complexNo += 1
            houseCount = 0
            checkHouse(houseMap, i, j, N)
            houseNo.append(houseCount)

print(complexNo)        # 단지 수
for n in sorted(houseNo):
    print(n)