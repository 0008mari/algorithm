# [boj 14891] [Python] 톱니바퀴
[문제 링크](https://www.acmicpc.net/problem/14891)

구현 문제. 제시된 조건이 길다. 헷갈릴만한 요소가 있으니까 차분히 전부 읽고 문제를 풀어야 함. 생각 못 한 것 때문에 한참 헤맸다.

문제를 풀고 나서 남의 코드를 보니까 deque를 사용한다. rotate가 있고 앞뒤로 삽입 삭제 가능하다는 점에서 매우 탁월한 선택인 듯 하다. 나는 떠올리지 못해서 리스트 사용했다. 그래서 아래 코드를 보면 rotate 해주는 함수를 직접 구현.

내가 헷갈린 조건은 다음과 같다.

*톱니바퀴 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면, B는 A가 회전한 방향과 반대방향으로 회전하게 된다.*

나는 이걸 얼핏 보고, 회전 먼저 적용 -> 회전 후의 톱니바퀴를 기준으로 옆에꺼에 영향을 줌
이렇게 생각했는데, 회전 전의 톱니바퀴가 기준이다. 이걸 대체 어떻게 수정하지 싶었는데, 의외로 간단하게 수정이 되었다. 톱니바퀴를 돌려서 바꾸는 부분과 영향주는 함수 호출하는 부분 순서를 바꾸면 되었다.

영향 주는 데에 있어서는 양 옆 방향으로 재귀함수 2개 이용.

코드는 아래와 같다.

```python
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
```

오늘의 문제 끝.