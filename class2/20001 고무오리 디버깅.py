# 20001 고무오리 디버깅

str = input() # 고무오리 디버깅 시작
stack = []

while (True):
    str = input()
    if (str == "고무오리 디버깅 끝"):
        break
    if (str == "문제"):
        stack.append(1)
    if (str == "고무오리"):
        if (len(stack)==0):
            stack.append(1)
            stack.append(1)
        else:
            stack.pop()

if (len(stack)==0):
    print("고무오리야 사랑해")
else:
    print("힝구")