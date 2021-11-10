# 1676 팩토리얼 0의 개수

def theNumberOfZero(num):
    cnt = 0
    while (num >= 5):
        cnt += num // 5
        num /= 5
    return int(cnt)

N = int(input())
print(theNumberOfZero(N))
