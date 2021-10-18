N = int(input())

ans = 0

for i in range(N):
    decomp = i
    n = i
    while(n > 0):
        decomp += n % 10
        n //= 10
    # print("i:", i, "decomp:", decomp)
    if (decomp == N):
        ans = i
        break

print(ans)
