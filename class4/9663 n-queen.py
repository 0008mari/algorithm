# 9663 엔퀸문제

def promising(i, col):
    k = 1
    flag = True
    while(k<i and flag):
        if col[i] == col[k] or abs(col[i]-col[k]) == (i-k):
            flag = False
        k += 1
    return flag


def n_queen(i, col):
    n = len(col) - 1
    if promising(i, col):
        if i==n:
            global result
            result += 1
        else:
            for j in range(1, n+1):
                col[i+1] = j
                n_queen(i+1, col)


n = int(input())
col = [0] * (n+1)
result = 0
n_queen(0, col)
print(result)
