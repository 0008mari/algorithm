# 17219 비밀번호 찾기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

mypass = dict()

for i in range(N):
    str = input().rstrip().split()
    mypass[str[0]] = str[1]

for i in range(M):
    str = input().rstrip()
    print(mypass.get(str))