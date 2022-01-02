# boj 1339 단어 수학
# 이코테 책에 있는 건 아닌데 
# 그리디 추가 문제 풀려고 태그로 찾았음

n = int(input())
words = []
for i in range(n):
    words.append(input())

# 이차원배열로 변환
words = list(map(list, words))
# 가장 길이가 긴 len 찾기
lenlist = map(len, words)
maxlen = max(lenlist)
# maxlen 기준으로 stuff (자리수 맞추기)
# stuffing - 0으로 (not alphabet)
for word in words:
    while (len(word)!=maxlen):
        word.insert(0, '0')
# 회전
newarr = list(zip(*words[::-1]))
# print(newarr)
result = 0
alphaDict = {}
digit = 9
ten = len(newarr) - 1   # 10의자릿수
for value in newarr:
    curdigits = []   # 현재 자릿수의 digit들 
    for char in value:
        if char.isdigit():
            continue
        # alphabet only
        if char in alphaDict:
            curdigits.append(alphaDict.get(char))
        else:
            alphaDict[char] = digit
            curdigits.append(digit)
            digit -= 1
    result += sum(curdigits) * ( 10 ** ten)
    ten -= 1

print(result)


# 틀렷음 걍 이렇게 풀면 안됨.
