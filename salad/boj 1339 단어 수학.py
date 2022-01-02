# boj 1339 단어 수학
# 이코테 책에 있는 건 아닌데 
# 그리디 추가 문제 풀려고 태그로 찾았음

n = int(input())
words = []
for i in range(n):
    words.append(input())

alphaDict = {}
# key- 알파벳, value - 자릿값(의 합)
digit = 9

for word in words:
    for j in range(len(word)):
        if word[j] in alphaDict:
            # 자릿수 곱해서 추가
            alphaDict[word[j]] += 10 ** (len(word)-j-1)
        else:
            alphaDict[word[j]] = 10 ** (len(word)-j-1)

numList = list(alphaDict.values())
numList = sorted(numList, reverse=True)

result = 0
digits = 9
for num in numList:
    result += digits * num
    digits -= 1

print(result)

