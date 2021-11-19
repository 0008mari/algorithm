# 2630 색종이 만들기

# global
paperCnt = [0, 0]

def isAllSame(ar, i, j, n):
    cnt = 0
    for a in range(n):
        for b in range(n):
            cnt += ar[i+a][j+b]
            
    if cnt == 0:
        return 0
    elif cnt == n*n:
        return 1
    else:
        return -1


def getQuardTree(ar, i, j, n):
    # input: i, j = start index
    # n = length of the side

    flag = isAllSame(ar, i, j, n)

    if (flag!=-1):
        paperCnt[flag] += 1
    else:
        getQuardTree(ar, i, j, n//2)
        getQuardTree(ar, i, j+n//2, n//2)
        getQuardTree(ar, i+n//2, j, n//2)
        getQuardTree(ar, i+n//2, j+n//2, n//2)


# main
N = int(input())
qt = [[0 for j in range(N)] for i in range(N)]

for i in range(N):
    tmp = input()
    for j in range(N):
        qt[i] = list(map(int, tmp.rsplit()))

getQuardTree(qt, 0, 0, N)
print(paperCnt[0], paperCnt[1], sep='\n')