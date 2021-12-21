# 문자열 뒤집기 

flag = 0    # 0 or 1
s = input()

count = 0
prev = s[0]
for c in s:
    if c == prev:
        continue
    else:
        count += 1
        prev = c

print(int(count/2+0.5))