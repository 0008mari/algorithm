# 3:18~

n = int(input())

stairs = [0] * 300
for i in range(0, n):
    stairs[i] = int(input())

# i칸 도달하는 경우의 수
# 1. i-2 -> i칸
# 2. i-3 -> i-1 -> i칸 
# 이 2가지 case로 이루어져 있다.
d = [0]*300
d[0] = stairs[0]
d[1] = stairs[0] + stairs[1]
d[2] = stairs[2] + max(stairs[0], stairs[1])
# d[i]: i 번째 계단에 오르는 가장 점수가 높은 방법.
# 연속 3번 방지? *** 
for i in range(3, n):
    d[i] = max(d[i-2], d[i-3] + stairs[i-1]) + stairs[i]

print(d[n-1])