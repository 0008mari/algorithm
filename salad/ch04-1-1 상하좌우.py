# 상하좌우 

N = int(input())
commands = input().split()

def isvaild(command, col, row):
    if command == "R":
        if row == N:
            return False
    elif command == "L":
        if row == 1:
            return False
    elif command == "U":
        if col == 1:
            return False
    else:   # "D"
        if col == N:
            return False
    return True



    
col = 1
row = 1

for command in commands:
    if not isvaild(command, col, row):
        continue
    if command == "R":
        row += 1
    elif command == "L":
        row -= 1
    elif command == "U":
        col -= 1
    else:   # "D"
        col += 1

print(col, row)
