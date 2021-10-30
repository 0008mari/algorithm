# 10866 덱
import sys
from typing import Deque

deque = []

def isEmpty():
    if len(deque)==0:
        return True
    else:
        return False

def push_front(X):
    deque.insert(0, X)

def push_back(X):
    deque.append(X)

def pop_front():
    if isEmpty():
        print("-1")
    else:
        x = deque.pop(0)
        print(x)

def pop_back():
    if isEmpty():
        print("-1")
    else:
        x = deque.pop()
        print(x)        

def size():
    print(len(deque))

def empty():
    if isEmpty():
        print("1")
    else:
        print("0")

def front():
    if isEmpty():
        print("-1")
    else:
        print(deque[0])

def back():
    if isEmpty():
        print("-1")
    else:
        print(deque[-1])


N = int(sys.stdin.readline())


for i in range(N):
    str = list(sys.stdin.readline().split())
    if str[0] == "push_front":
        push_front(int(str[1]))
    elif str[0] == "push_back":
        push_back(int(str[1]))    
    elif str[0] == "pop_front":
        pop_front()
    elif str[0] == "pop_back":
        pop_back()
    elif str[0] == "size":
        size()
    elif str[0] =="empty":
        empty()
    elif str[0] == "front":
        front()
    elif str[0] == "back":
        back()