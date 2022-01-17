
def isValid(n, m, i, j):
    if i < 0 or i >= n or j < 0 or j >= m:
        return False
    return True


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arrFlat = list(map(int, input().split()))
    arr = [[0] for i in range(n)]
    
    for i in range(n):
        tmp = []
        for j in range(m):
            tmp.append(arrFlat[i*m + j])
        arr[i] = tmp
    # 입력 완료

    # 금 정보를 담은 배열을 갱신해가며, 3가지 경우 중 max를 저장한다.
    for j in range(1, m):
        for i in range(n):
            # if case - index 오류 처리
            if i == 0:
                arr[i][j] = max(arr[i][j-1] + arr[i][j], arr[i+1][j-1] + arr[i][j])
            elif i == n-1:
                arr[i][j] = max(arr[i-1][j-1] + arr[i][j], arr[i][j-1] + arr[i][j])
            else:
                # 해당 없음, 3가지 중 max 찾기
                arr[i][j] = max(arr[i-1][j-1] + arr[i][j], arr[i][j-1] + arr[i][j], arr[i+1][j-1] + arr[i][j])
    
    rst = min(map(min, arr))
    # 2차원이라 min 2번
    print(rst)


