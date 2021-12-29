from collections import deque

def divide(p):
    stack = deque()
    first = p[0]
    stack.append(p[0])
    i = 1
    while stack:
        # 스택이 빌 때까지
        if p[i] == first:
            stack.append(p[i])
        else:
            stack.pop()
        i += 1
    u = p[:i]
    v = p[i:]
    return u, v

def isRight(p):
    # 올바른 괄호 문자열인가?
    stack = deque()
    for i in range(len(p)):
        if p[i] == "(":
            stack.append("(")
        else:
            if not stack:
                # if it is empty
                return False
            stack.pop()
    if stack:
        # 내용물이 남아있으면
        return False
    else:
        return True

def reverse(strings):
    r = {"(":")", ")":"("}
    return "".join([r[s] for s in strings])

def recursion(p):
    if len(p) == 0:
        return ""
    
    # u, v로 분리
    u, v = divide(p)
    if isRight(u):
        return u + recursion(v)
    else:
        str = "("
        str += recursion(v)
        str += ")"
        str += reverse(u[1:-1])
        return str

def solution(p):
    
    answer = recursion(p)
    
    
    return answer

print(solution("()))((()"))