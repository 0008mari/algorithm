# 1181 단어 정렬

N = int(input())
ar = []
for i in range(N):
    tmp = input()
    ar.append(tmp)

ar = set(ar)
ar = sorted(ar)
ar = sorted(ar, key=len)
for i in range(len(ar)):
    print(ar[i])