# 11050 이항계수 1
N, K = map(int, input().split())

m = max(N, K)
BiCo = [[1 for j in range(m+1)] for i in range(m+1)]


def getBinomalCoefficient(n, r):
    if (n == r or r == 0):
        return 1
    else:
        # print(BiCo[n-1][r-1], BiCo[n-1][r])
        return BiCo[n-1][r-1] + BiCo[n-1][r]


for i in range(N+1):
    for j in range(i+1):
        # print("i=", i, "j=", j)
        BiCo[i][j] = getBinomalCoefficient(i, j)
        if (i==N and j ==K):
            break

print(BiCo[N][K])
