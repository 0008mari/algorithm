# 1541 잃어버린 괄호

line = input()

operands = list(map(int, line.replace('-', '+').split(sep='+')))
operators = []
operators.append('+')

for char in line:
    if char.isdigit():
        continue
    else:
        operators.append(char)



i, j = 0, 0
for i in range(len(operands)):
    j = i
    if operators[j] == '-':
        if j < len(operators)-1:
            k = j + 1
            while(operators[k]!='-'):
                operands[i] += operands[k]
                operands[k] = 0
                k += 1
                if k == len(operators):
                    break
        operands[i] = -1 * operands[i]

print(sum(operands))
