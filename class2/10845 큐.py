# 10845 큐
import sys


queue = []
len = 0

def isEmpty():
    if len == 0:
        return True
    else:
        return False

def push(X):
    global len
    queue.append(X)
    len += 1

def pop():
    global len
    if isEmpty():
        print("-1")
    else:
        x = queue.pop(0)
        print(x)
        len -= 1

def size():
    print(len)

def empty():
    if isEmpty():
        print("1")
    else:
        print("0")

def front():
    if isEmpty():
        print("-1")
    else:
        print(queue[0])

def back():
    if isEmpty():
        print("-1")
    else:
        print(queue[-1])


N = int(sys.stdin.readline())


for i in range(N):
    str = list(sys.stdin.readline().split())
    if str[0] == "push":
        tmp = int(str[1])
        push(tmp)
    elif str[0] == "pop":
        pop()
    elif str[0] == "size":
        size()
    elif str[0] =="empty":
        empty()
    elif str[0] == "front":
        front()
    elif str[0] == "back":
        back()