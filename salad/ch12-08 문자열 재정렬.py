s = input()
digitsum = 0

result = []

for c in s:
    if c.isdigit():
        digitsum += int(c)
    elif c.isascii():
        result.append(c)

result = sorted(result)

print(''.join(result)+str(digitsum))

