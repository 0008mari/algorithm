# 실패율
# 프로그래머스 



def solution(N, stages):
    answer = []
    length = len(stages)

    # 모든 스테이지에 대해
    for stage in range(1, N+1):
        # 해당 스테이지에있는사람들
        count = stages.count(stage)
        
        if length == 0:
            fail = 0
        else:
            fail = count/length
        
        answer.append((stage, fail))
        length -= count
        # 이전 스테이지에 머물러 있는 애들은
        # 다음 스테이지에 도달하지 못했을테니
        # 도달 수에서 빼는 것.

    answer = sorted(answer, key=lambda t: t[1], reverse=True)

    answer = [i[0] for i in answer]
    return answer
    
# solution(5, [2,1,2,6,2,4,3,3])