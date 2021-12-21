place = input()
# a4 이런식으로
# 행 1..8, 열 a..h

col = ord(place[0]) - ord('a') + 1
row = int(place[1])

count = 0

def isvalid(col, row):
    if col<1 or row <1 or col > 8 or row > 8:
        return False
    else:
        return True

if (isvalid(col+1, row+2)):
    count += 1
if (isvalid(col+1, row-2)):
    count += 1

if (isvalid(col-1, row+2)):
    count += 1
if (isvalid(col-1, row-2)):
    count += 1

if (isvalid(col+2, row-1)):
    count += 1
if (isvalid(col+2, row+1)):
    count += 1

if (isvalid(col-2, row+1)):
    count += 1
if (isvalid(col-2, row-1)):
    count += 1

print(count)