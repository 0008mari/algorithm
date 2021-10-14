# 15829 Hashing

M = 1234567891
r = 31


L = int(input())
str =  input()

# string을 char 단위로 나누고
# 각 문자를 list의 원소로 저장. 
list = list(str)

# 각 char를 숫자로 변환. 

# raw_input 입력받은 결과에 상관없이 무조건 string으로 간주
# raw_input은 python 3에서 삭제되었음
# 대신 str으로 직접 변환

list2 = []

# 순회하며 각 문자에 ord 적용
for char in list:
    num = ord(char) - 96
    list2.append(num)


# 그다음 해시 적용

for i in range(len(list2)):
    list2[i] = list2[i] * (r ** i)

sum = sum(list2)
H = sum % M

print(H)