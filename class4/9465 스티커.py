# 2트 - dp
# 9465 스티커

T = int(input())
for _ in range(T):
    n = int(input())
    arr = [[0] for _ in range(2)]
    for i in range(2):
        arr[i] = list(map(int, input().split()))
    
    for row in range(1, n):
        if row == 1:    #처음시작 시 
            arr[0][row] += arr[1][row-1]
            arr[1][row] += arr[0][row-1]
        else:   # 일반적인 경우에
            arr[0][row] += max(arr[1][row-1], arr[1][row-2])
            arr[1][row] += max(arr[0][row-1], arr[0][row-2])
    
    print(max(arr[0][n-1], arr[1][n-1]))