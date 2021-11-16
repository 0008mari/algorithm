# 1992 쿼드트리

# NOT OPTIMIZED (TIME)







import sys
input = sys.stdin.readline

# global
paperCount = [0, 0, 0]

# def isAllSame(ar, i, j, n):
#     check = ar[i][j]
#     for a in range(n):
#         for b in range(n):
#             if check != ar[i+a][j+b]:
#                 return -2
#     return check


def getPaperNum(ar, i, j, n):
    # input: i, j = start index
    # n = length of the side

    # flag = isAllSame(ar, i, j, n)

    flag = paperMat[i][j]
    for x in range(n):
        for y in range(n):
            if paperMat[i+x][j+y] != flag:
                offset = n//3
                getPaperNum(ar, i, j, offset)
                getPaperNum(ar, i, j+offset, offset)
                getPaperNum(ar, i, j+2*offset, offset)

                getPaperNum(ar, i+offset, j, offset)
                getPaperNum(ar, i+offset, j+offset, offset)
                getPaperNum(ar, i+offset, j+2*offset, offset)

                getPaperNum(ar, i+2*offset, j, offset)
                getPaperNum(ar, i+2*offset, j+offset, offset)
                getPaperNum(ar, i+2*offset, j+2*offset, offset)
                return
                
    paperCount[flag]+=1
    return



# main
N = int(input())
paperMat = [[0 for j in range(N)] for i in range(N)]

for i in range(N):
    tmp = input()
    for j in range(N):
        paperMat[i] = list(map(int, tmp.rsplit()))

getPaperNum(paperMat, 0, 0, N)

print(paperCount[2], paperCount[0], paperCount[1], sep='\n')