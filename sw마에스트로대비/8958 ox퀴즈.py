# OX퀴즈

t = int(input())
for i in range(t):
    s = input()
    cnt = 0
    rst = 0
    for j in s:
        if j == 'X':
            cnt = 0
        elif j == 'O':
            cnt += 1
            rst += cnt
    print(rst)
