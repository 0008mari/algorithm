def rotation(arr):
    n = len(arr)
    ret = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            ret[j][n-1-i] = arr[i][j]
    return ret

def checkKeyLock(key, lock, a, b, N, M):
    # input: start location of key a, b
    check = True
    for i in range(M):
        for j in range(M):
            if i < 0 or i >= N or j < 0 or j >= N:
                # 자물쇠 영역 밖은 검사하지 않음
                continue
            if key[i+a][j+b] != lock[i][j]:
                return False
    return True


def solution(key, lock):
    N = len(lock)
    M = len(key)

    for r in range(0, 4):
        for a in range(N-M+1, N+M):
            for b in range(N-M+1, N+M):
                if checkKeyLock(key, lock, a, b, N, M):
                    return True
        key = rotation(key)        


    return False