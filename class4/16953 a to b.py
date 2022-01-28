# A -> B
# 16953 

a, b = map(int, input().split())

# 최대 50
# 가지를 어떻게 표현하지 

rst = -1

def recursion(result, goal, depth):
    if result > goal:
        return
    elif result == goal:
        global rst
        rst = depth+1
        return

    recursion(result*2, goal, depth+1)
    recursion(result*10+1, goal, depth+1)


recursion(a, b, 0)
print(rst)