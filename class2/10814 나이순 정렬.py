# 10814 나이순 정렬


N = int(input())

member = [["\0" for i in range(2)] for j in range(N)]

for i in range(N):
    member[i] = list(input().split())

# member_s = member

map(lambda row: map(int, row), member)

member_s = member 

print(member_s)

member_s = sorted(member_s, key=lambda x: x[0])


for i in range(N):
    print(member_s[i][0], member_s[i][1])   

