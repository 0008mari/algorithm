# 11650 좌표 정렬하기

N = int(input())

ar = [[0 for i in range(2)] for j in range(N)]

for i in range(N):
    ar[i] = (list)(map(int, input().split()))

# ar2 = sorted(ar, key=lambda x:x[0])
# ar2 = sorted(ar, key=lambda x:x[1])

ar2 = sorted(ar)

# print(ar)

for i in range(N):
    print(ar2[i][0], ar2[i][1])

# for row in ar2:
#     for col in row:
#         print(col, end=' ')
#     print()
 
