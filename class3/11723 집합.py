# 11723 집합

import sys

# global
s = set()
al = set(range(1, 21))

def check(x):
    if x in s: 
        print("1")
    else:
        print("0")


def toggle(x):
    if x in s:
        s.discard(x)
    else:
        s.add(x)


M = int(input())

for i in range(M):
    str = sys.stdin.readline().rstrip().split()
    if str[0] == "add":
        s.add(int(str[1]))
    elif str[0] == "remove":
        s.discard(int(str[1]))
    elif str[0]=="check":
        check(int(str[1]))
    elif str[0]=="toggle":
        toggle(int(str[1]))
    elif str[0]=="all":
        s = al
    elif str[0] == "empty":
        s = set()
    # print(s)
