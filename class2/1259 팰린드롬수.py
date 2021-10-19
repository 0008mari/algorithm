# 1259 팰린드롬수
# 팰린드롬수는 회문의 숫자 버전이다.

def isPalindrome(ar):
    start = 0
    end = len(ar) - 1

    while (start < end):
        if ar[start] == ar[end]:
            start += 1
            end -= 1
        else:
            return False
    return True


while (True):
    str = input()
    if str=="0":
        break
    rst = isPalindrome(str)
    if rst == True:
        print("yes")
    else:
        print("no")