# boj 1107

n = int(input())
M = int(input())

ans = abs(100 - n)
if M:
    broken = set(input().split())
else:
    broken = set()

for num in range(1000001): 
    for N in str(num):
        if N in broken:
            break
    else: 
    	ans = min(ans, len(str(num)) + abs(num - n))

print(ans)