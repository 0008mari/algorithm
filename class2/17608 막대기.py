# 17608 막대기
# stack

stack = []

N = int(input())

for i in range(N):
    a = int(input())
    stack.append(a)

# input end

p = stack[-1]
cnt = 1
for i in range(N):
    a = stack.pop()
    if (a > p):
        cnt += 1
        p = a

print(cnt)

