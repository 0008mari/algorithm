
def getResidentNum(k, n):
    apt = [[0 for i in range(n+2)] for j in range(k+1)]
    for i in range(1, n+1):
        apt[0][i] = i   # 0층
    for i in range(1, k+1):
        for j in range(1, n+1):
            if (i-1 < 0):
                a = 0
            a = apt[i-1][j]

            if (j-1 <= 0):
                b = 0
            b = apt[i][j-1]

            apt[i][j] = a + b
    return apt[k][n]

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        k = int(input())
        n = int(input())

        print(getResidentNum(k, n))

