from itertools import combinations

def check(teachers, field):
    for teacher in teachers:
        ci, cj = teacher[0], teacher[1]
        while(ci>=0):                   # 좌 방향
            if field[ci][cj]=="O":
                break
            if field[ci][cj]=="S":
                return False
            ci -= 1
        ci, cj = teacher[0], teacher[1]
        while(ci< len(field)):        # 우 방향
            if field[ci][cj]=="O":
                break
            if field[ci][cj]=="S":
                return False
            ci += 1
        ci, cj = teacher[0], teacher[1]
        while(cj >= 0):                 # 상 방향
            if field[ci][cj]=="O":
                break
            if field[ci][cj]=="S":
                return False
            cj -= 1
        ci, cj = teacher[0], teacher[1]
        while(cj< len(field)):        # 하 방향
            if field[ci][cj]=="O":
                break
            if field[ci][cj]=="S":
                return False
            cj += 1 
    return True


n = int(input())
field = [ [] for _ in range(n)]
for i in range(n):
    field[i] = list(input().split())

# 선생님 위치 미리 파악
teachers = []
for i in range(n):
    for j in range(n):
        if field[i][j] == "T":
            teachers.append([i, j])

results = []

for objects in combinations(range(0, n*n), 3):
    if field[objects[0]//n][objects[0]%n] != "X" or field[objects[1]//n][objects[1]%n] != "X" or field[objects[2]//n][objects[2]%n] != "X":
        continue
        # 이 조합은 체크 x (불가함)
    # 가공
    field[objects[0]//n][objects[0]%n] = "O"
    field[objects[1]//n][objects[1]%n] = "O"
    field[objects[2]//n][objects[2]%n] = "O"
    # 검사
    results.append(check(teachers, field))
    # 복구
    field[objects[0]//n][objects[0]%n] = "X"
    field[objects[1]//n][objects[1]%n] = "X"
    field[objects[2]//n][objects[2]%n] = "X"
    
if True in results:
    print("YES")
else:
    print("NO")



