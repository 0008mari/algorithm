# 5430 AC

import sys
from collections import deque

T = int(input())

for i in range(T):
    flag = 0
    d = 1       # direction: 순 1, 역 -1
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    ar = sys.stdin.readline()[1:-2].split(",")

    if ar[0] != '':
        ar = deque(ar)
    else:
        ar = deque()


    for command in p:
        if command=="R":
            d *= -1
        elif command=="D":
            if len(ar)==0:
                flag = 1        # error
                break
            if d<0:
                ar.pop()
            else:
                ar.popleft()

    if flag==1:
        print("error")
    else:
        print("[", end='')

        if d>0:
            index = 0
            for c in ar:
                print(c, end='')
                if (index != len(ar)-1):
                    print(",", end='')
                    index += 1
        else:
            index = 0
            for c in reversed(ar):
                print(c, end='')
                if (index != len(ar)-1):
                    print(",", end='')
                    index += 1
        
        print("]")


