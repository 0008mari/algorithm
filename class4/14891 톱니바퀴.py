# 14891 톱니바퀴

S = 1
N = 0

left = -1
right = 1

gears = [[S, N, S, N, S, S, S, S],
        [N, S, S, S, S, S, N, S],
        [S, S, N, N, S, S, S, N],
        [N, N, N, N, N, N, S, N]]
# test sample

def clockwiseRotate(gear):
    # input: 1d list
    return [gear[-1]] + gear[:-1]


def antiClockwiseRotate(gear):
    return gear[1:] + [gear[0]]


def rotate(gear, d):
    if d == 1:
        return clockwiseRotate(gear)
    else:
        return antiClockwiseRotate(gear)


def gearEffect(n, v, d):
    if v == left and n != 1:
        if gears[n-2][2] != gears[n-1][6]:
            gearEffect(n-1, left, d*-1)
            gears[n-2] = rotate(gears[n-2], d*-1)
            return 
    if v == right and n != 4:
        if gears[n-1][2] != gears[n][6]:
            gearEffect(n+1, right, d*-1)
            gears[n] = rotate(gears[n], d*-1)
            return
    return
    # 영향 받고 양쪽으로 영향 전파 (재귀)
    

def gearRotate(n, d):
    gearEffect(n, left, d)
    gearEffect(n, right, d)
    gears[n-1] = rotate(gears[n-1], d)

# main
for i in range(4):
    gears[i] = list(map(int, list(str(input()))))

k = int(input())

for _ in range(k):
    n, d = map(int, input().split())
    gearRotate(n, d)

rst = 0
for i in range(4):
    rst += gears[i][0] * (2**i)
print(rst)
