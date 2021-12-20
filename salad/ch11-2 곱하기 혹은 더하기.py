s = input()
s = list(map(int, list(s)))

stack = []

stack.append(s[0])

for i in range(1, len(s)):
    if stack[0] == 0 or s[i] == 0:
        stack[0] = stack[0]+s[i]
    else:
        # 둘다 0 아닐때 곱셈
        stack[0] = stack[0]*s[i]

print(stack[0])
