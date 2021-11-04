# 1018: 체스판 다시 칠하기

bw = list('BWBWBWBW')
wb = list('WBWBWBWB')

def repaintNumberSub(n, ar, a, b):
    flag = n            # 0 or 1
    cnt = 0
    for i in range(8):      # compare each row
        if ((i+flag)%2==0):   # compare with bw
            for j in range(8):
                if (ar[a+i][b+j] != bw[j]):
                    cnt += 1
        else:               # compare with wb
            for j in range(8):
                if (ar[a+i][b+j] != wb[j]):
                    cnt += 1
    return cnt



def repaintNumber(bwin, i, j):
    cnt1 = repaintNumberSub(0, bwin, i, j)
    cnt2 = repaintNumberSub(1, bwin, i, j)
    return min(cnt1, cnt2)
            



N, M = map(int, input().split())
bwin = [['\0' for j in range(M)] for i in range(N)]

for i in range(N):
    bwin[i] = input()

rNum = [[0 for j in range(M-8+1)] for i in range(N-8+1)]

for i in range(N-8+1):
    for j in range(M-8+1):
        rNum[i][j] = repaintNumber(bwin, i, j)


mymin = min([min(r) for r in rNum])
print(mymin)
