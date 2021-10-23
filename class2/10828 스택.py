# 10828 스택

import sys


stack = []
global slen
slen = 0

def isEmpty():
    global slen
    if slen==0:
        return True
    else:
        return False 


def push(X):
    global slen
    stack.append(X)
    slen += 1


def pop():
    if isEmpty():
        print(-1)
    else:
        global slen
        print(stack.pop())
        slen -= 1


def size():
    global slen
    print(slen)


def empty():
    if isEmpty():
        print("1")
    else:
        print("0")


def top():
    if isEmpty():
        print("-1")
    else:
        print(stack[-1])


# main

N = int(sys.stdin.readline())
for i in range(N):
    str = sys.stdin.readline().rstrip().split()
    if str[0] == "push":
        tmp = int(str[1])
        push(tmp)
    elif str[0] == "pop":
        pop()
    elif str[0] == "size":
        size()
    elif str[0] == "empty":
        empty()
    elif str[0] == "top":
        top()