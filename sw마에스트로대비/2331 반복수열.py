# 2331 반복수열

def nextD(a, p):
    digits = list(map(int, list(str(a))))
    # print(digits)
    return sum(map(lambda x: x**p, digits))



a, p = map(int, input().split())

d = [a]

while True:
    now = nextD(d[-1], p)
    if now in d:
        break
    d.append(now)

print(d.index(now))



