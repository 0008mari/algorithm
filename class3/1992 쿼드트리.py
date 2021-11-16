# 1992 쿼드트리


# global
stack = []

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
    if (flag!=-1):      # recursive call
        stack.append(str(flag))
    else:
        stack.append("(")
        getQuardTree(ar, i, j, n//2)
        getQuardTree(ar, i, j+n//2, n//2)
        getQuardTree(ar, i+n//2, j, n//2)
        getQuardTree(ar, i+n//2, j+n//2, n//2)
        stack.append(")")


# main
N = int(input())
qt = [[0 for j in range(N)] for i in range(N)]

for i in range(N):
    tmp = input()
    for j in range(N):
        qt[i] = list(map(int, list(tmp)))

getQuardTree(qt, 0, 0, N)
print(''.join(stack))