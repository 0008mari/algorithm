import copy

def isValidTest(ground):
    # ground의 모든 원소에 대해 검사
    for i in range(0, len(ground)):
        for j in range(0, len(ground)):
            if ground[i][j] == -1:
                continue                # 아무것도 없음
            elif ground[i][j] == 0:     # 기둥
                if j == 0:
                    continue            # 바닥위, 통과
                if ground[i][j-1] == 0:
                    continue            # 다른 기둥 위, 통과
                if i-1>=0 and ground[i-1][j] == 1:
                    continue            # 보의 끝 위(1)
                if ground[i][j] == 1:
                    continue            # 보의 끝 위(2)
            elif ground[i][j] == 1:     # 보
                if i-1>=0 and ground[i-1][j] == 0:
                    continue            # 기둥 위
                if ground[i-1][j+1] == 0:
                    continue            # 기둥 위
                if ground[i][j-1] == 1 and ground[i][j+1] == 1:
                    continue
            else:
                return False
    return True


def isValidDelete(x, y, a, ground):    
    tmpGround = copy.deepcopy(ground)
    tmpGround[x][y] = -1
    # 지워보고 오류 검사
    if isValidTest(tmpGround):
        ground[x][y] = -1
        return True
    else:
        return False


def isValidBuild(x, y, a, ground):
    tmpGround = copy.deepcopy(ground)
    tmpGround[x][y] = a
    # 만들어보고 오류 검사
    if isValidTest(tmpGround):
        ground[x][y] = a
        return True
    else:
        return False


def isValid(x, y, a, b, ground):
    if b == 0:
        return isValidDelete(x, y, a, ground)
    else:
        return isValidBuild(x, y, a, ground)


def execute(command, ground):
# input: [x, y, a, b] 형태
    x = command[0]
    y = command[1]
    a = command[2]
    b = command[3]
    if not isValid(x, y, a, b, ground):
        return
    else:
        if b == 0:
            ground[x][y] = -1
        else:
            ground[x][y] = a
    


def getAnswer(ground):
    answer = []
    for i in range(0, len(ground)):
        for j in range(0, len(ground)):
            if ground[i][j] != -1:
                tmp = []
                tmp.append(i)
                tmp.append(j)
                tmp.append(ground[i][j])
                answer.append(tmp)
    print(answer)
    return answer

def solution(n, build_frame):

    ground = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    # 현재 공사 상태
    # ground[x][y] = 0 이렇게 표현, -1: 아무것도 없음

    for command in build_frame:
        execute(command, ground)

    answer = getAnswer(ground)

    return answer



# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
# n = 5

# solution(n, build_frame)