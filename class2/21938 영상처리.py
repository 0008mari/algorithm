# 21938번: 영상처리
import sys
sys.setrecursionlimit(10**6)


def pixelThresholding(T, r, g, b):
    avg = (r + g + b)/3
    if avg>=T:
        return 255
    else:
        return 0

'''
def udlrCleanChecker(ar, i, j, N, M):
    # up down left right 
    # pixel 
    if (i>0):
        if (ar[i-1][j] > 0):
            return i-1, j
    if (i<N):
        if (ar[i+1][j] > 0):
            return i+i, j
    if (j>0):
        if (ar[i][j-1] > 0):
            return i, j-1
    if (j<M):
        if (ar[i][j+1] > 0):
            return i, j+1
    return -1, -1
'''



def udlrClear(th, i, j, N, M):
    th[i][j]=0
    # if (i>0):
    #     th[i-1][j] = 0
    # if (i<N-1):
    #     th[i+1][j] = 0
    # if (j>0):
    #     th[i][j-1] = 0
    # if (j<M-1):
    #     th[i][j+1] = 0

def udlrAllClear(th, i, j, N, M):
    udlrClear(th, i, j, N, M)
    if (i>0):
        if (th[i-1][j] > 0):
            udlrAllClear(th, i-1, j, N, M)
    if (i<N-1):
        if (th[i+1][j] > 0):
            udlrAllClear(th, i+1, j, N, M)
    if (j>0):
        if (th[i][j-1] > 0):
            udlrAllClear(th, i, j-1, N, M)
    if (j<M-1):
        if (th[i][j+1] > 0):
            udlrAllClear(th, i, j+1, N, M)
    


N, M = map(int, input().split())
# for i in range(N):
#     for j in range(M):
#         for k in range(3):
#             print(i, j, k)
#             nm[i][j][k] = int(input())

nm = [[[0 for k in range(3)] for j in range(M)] for i in range(N)]


for i in range(N):
    num_list = list(map(int, input().split()))
    idx = 0
    for j in range(M):
        for k in range(3):
            # print(i, j, k)
            nm[i][j][k] = num_list[idx]
            idx += 1


T = int(input())
# 입력 완료

# step 1. pixel Thresholding
th = [[0 for j in range(M)] for i in range(N)]
for i in range(N):
    for j in range(M):
        th[i][j] = pixelThresholding(T, nm[i][j][0], nm[i][j][1], nm[i][j][2])

# step 2. object detection
cnt = 0
for i in range(N):
    for j in range(M):
        if th[i][j] == 0:
            continue
        else:
            cnt += 1
            udlrAllClear(th, i, j, N, M)
            

# step 3. print
print(cnt)


# 재귀 가자 

