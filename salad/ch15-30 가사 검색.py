# 천재 프로그래머 프로도 
# 와일드카드 문자열

# 접두사는 앞에 ??? 만큼 썰고 보고 
# (word는 10만개라 삽가능)
# 접미사는 앞엣글자 기준으로 
# 이진탐색 (키워드 1000000개 ㅅ)

# 첫글자 기준으로 탐색하고
# 첫글자가 같으면 그 뒤

from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

# 모든 단어를 길이마다 나누어서 저장
array = [[] for _ in range(10001)]
# 모든 단어를 길이마다 나누어서 뒤집어 저장
reversed_array = [[] for _ in range(10001)]


def solution(words, queries):
    answer = []
    
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()
    
    for q in queries:
        if q[0] != '?':
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)