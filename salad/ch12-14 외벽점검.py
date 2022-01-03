# 이코테 책 정답

from itertools import permutations

def solution(n, weak, dist):
    # 배열 일자로 만들기 ㄷㄷ 
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist)+1    # 최솟값이 답이니까 최댓값으로 초기화
    # 0부터 length-1 까지의 위치를 시작점으로 설정
    for startPoint in range(length-1):
        for friends in list(permutations(dist, len(dist))):
            count = 1   # 투입할 친구 수 
            position = weak[startPoint] + friends[count-1]
            # position - 해당 친구가 점검할 수 있는 마지막 위치
            for index in range(startPoint, startPoint + length):
                if position < weak[index]:
                    # 해당 친구가 점검 불가하면
                    count += 1
                    # 새 친구 투입
                    if count > len(dist):
                        break   # 더이상 투입 불가하면 종료 (실패)
                    position = weak[index] + friends[count-1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer

solution(12, [1,5,6,10], [1,2,3,4])