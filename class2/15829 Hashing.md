# 15829 Hashing

10월 14일

기본적인 해싱 문제이다. 해싱보다는 아래 조건 변환하는 방법만 살펴본다.

> 먼저, 편의상 입력으로 들어오는 문자열에는 영문 소문자(a, b, ..., z)로만 구성되어있다고 가정하자. 영어에는 총 26개의 알파벳이 존재하므로 a에는 1, b에는 2, c에는 3, ..., z에는 26으로 고유한 번호를 부여할 수 있다. 결과적으로 우리는 하나의 문자열을 수열로 변환할 수 있다. 예를 들어서 문자열 "abba"은 수열 1, 2, 2, 1로 나타낼 수 있다.



C 였으면 `c - 'A'` 했을 텐데 파이썬에서는 처음 본다.

스택오버플로우에 답이 있다. [참고한 링크](https://stackoverflow.com/questions/4528982/convert-alphabet-letters-to-number-in-python)



```python
L = int(input())
str =  input()

# string을 char 단위로 나누고
# 각 문자를 list의 원소로 저장.
# list()의 인자로 문자열을 넣으면 자동으로 해준다.
list = list(str)

# 각 char를 숫자로 변환. 
# 순회하며 각 문자에 ord 적용
list2 = []
for char in list:
    num = ord(char) - 96
    list2.append(num)
```



참고사항

* raw_input()은 입력 받은 데이터의 종류에 상관 없이 문자열로 간주하는 입력함수이다. 그러나 이것은 Python2의 이야기이고, Python3에서는 이 raw_input()이 그냥 `input()`이 되었다. 
* 따라서 수를 받고자 하면 `int(input())`을 사용한다. 
* `ord()`는 유니코드 문자를 인자로 받아 유니코드 숫자로 바꿔준다. 'a'는 96이 된다. [ord - docs.python](https://docs.python.org/3/library/functions.html#ord)



전체 코드

```python
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
```



