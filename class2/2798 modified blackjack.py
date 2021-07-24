N, M = map(int, input().split())

str = input() # 카드 값들 나열된 문자열
list = map(int, str.split())
# 문자열을 정수 리스트로 변환

# 그리디 

sum = 0

# 오름차순 정렬
list2 = sorted(list)
# print(list2)

def modifiedBlackjack(list):
    sum = 0
    ans = 0
    for i in range(N):
        for j in range(i):
            for k in range(j):
                sum = list[i] + list[j] + list[k]
                if (sum <= M):
                    if (ans < sum):
                        ans = sum
    return ans

# def modifiedBlackjack(list2):
    sum = 0
    ans = 0
    for i in reversed(range(N)):
        sum = list2[i]
        if (sum > M):
            continue
        for j in reversed(range(i)):
            sum = list2[i] + list2[j]
            if (sum > M):
                continue
            for k in reversed(range(j)):
                sum = list2[i] + list2[j] + list2[k]
                if (sum > M):
                    continue
                print("Hi:", list2[i], list2[j], list2[k])
                if (ans < sum):
                    ans = sum
    
    return ans

print(modifiedBlackjack(list2))

                
            
