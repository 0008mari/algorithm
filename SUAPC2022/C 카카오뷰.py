n = int(input())
interests = list(map(int, input().split()))
isRegistered = list(map(int, input().split()))

r1 = 0
r2 = 0

for i in range(n):
    if not isRegistered[i]:
        r2 += interests[i]
    r1 += interests[i]

print(r1, r2, sep='\n')
