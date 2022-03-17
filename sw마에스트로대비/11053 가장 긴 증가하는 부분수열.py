# 11053 가장 긴 증가하는 부분수열

n = int(input())
a = list(map(int, input().split()))

d = [1] * (n)

for i in range(n):
    for j in range(0, i):
        if a[j]<a[i]:
            d[i] = max(d[i], d[j]+1)
            
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
print(max(d))
