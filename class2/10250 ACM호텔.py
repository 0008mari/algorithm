T = int(input())

for i in range(T):
    # input
    H, W, N = map(int, input().split())


    h = N % H
    if (h == 0):
        h = H

    w = N//H + 1
    if (N % H == 0):
        w -= 1

    ans = h*100 + w

    print(ans)