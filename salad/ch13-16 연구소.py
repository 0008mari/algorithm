def isValid(i, j, N, M):
    # input: location i, j
    # size N, M
    # output: is it valid?
    if i < 0 or i > N-1 or j < 0 or j > M-1:
        return False
    else:
        return True

def dfs():
    # output: number of 0s (virused)

def findSafeDimesion(labMap, n, m):
    # input
    # output: size of safeDivision
    virusPosition = []
    safeDimensions = []
    for i in range (n):
        for j in range(m):
            if labMap(i, j) == 2:
                virusPosition.append([i, j])

    for position in virusPosition:
        safeDimensions.append()

    

# main
n, m = map(int, input().split())
labMap = [[0 for _ in range(n)] for _ in range(m)]

# input
for i in range(n):
    labMap[i] = map(int, input().split())


