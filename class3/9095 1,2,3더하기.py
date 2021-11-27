# 9095 1,2,3더하기


def A(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return A(n-1) + A(n-2) + A(n-3)



T = int(input())
for i in range(T):
    n = int(input())
    result = A(n)
    print(result)



