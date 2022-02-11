# 1080 행렬

def isEqual(n, m, a, b):
    # matrix a, b size of n*m
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return False
    return True

def reverse(a, n, m, i, j):
    # matrix a,
    # start position a[i][j]
    if i<=n-3 and j <=m-3:
        for x in range(3):
            for y in range(3):
                a[i+x][j+y] = (a[i+x][j+y] + 1) % 2
                # 0, 1 toggle
    return a


### main

n, m = map(int, input().split())
a = [[0] for _ in range(n)]
b = [[0] for _ in range(n)]

for i in range(n):
    a[i] = list(map(int, list(str(input())))) 
for i in range(n):
    b[i] = list(map(int, list(str(input())))) 


cnt = 0
flag = 0
for i in range(n):
    for j in range(m):
        if isEqual(n, m, a, b):
            flag = 1
            break
        if a[i][j] != b[i][j]:
            a = reverse(a, n, m, i, j)
            cnt += 1

if flag:
    print(cnt)
else:
    print(-1)