# 외벽점검 - 구현

# 버리는코드 

from itertools import combinations

def goAhead(current, direction, n):
    # 원형 전진
    # direction 1: 시계, -1: 반시계 한칸앞으로
    return (current+direction+n)%n

def weakPointCheck(members, weak, dist, covered, n):
    for startpoint in weak:
        current = startpoint
        for direction in [-1, 1]:
            for member in members:
                ahead = dist[member]
                if current in weak:
                    covered[weak.index(current)] = True
                # 전진횟수만큼 전진
                for _ in range(ahead):
                    # 현재 위치가 weakpoint이면
                    if current in weak: # 방문 처리
                        covered[weak.index(current)] = True
                    # 전진
                    current = goAhead(current, direction, n)
                    # 완전한지 검사
                    if False not in covered:
                        return




                
    print(members)


def solution(n, weak, dist):
    answer = 0
    direction = [-1, 1]
    for i in range(1, len(dist)):
        # 조합 선택할 인원수: i
        for selections in combinations(sorted(dist, reverse=True), i):
            # 각 selections 별로 모든 노드에서 시작시킴
            covered = [False for _ in range(len(weak))]
            weakPointCheck(selections, weak, dist, covered, n)
            print("foo")
            if False not in covered:  # 커버 성공
                break

        if False not in covered:
            break       # 한번 더 break
    
    print(i)

    return answer



# 이거 콤비네이션 할 필요 없고
# 그냥 제일큰dist부터 1개->2개 이렇게 가면 됨


solution(12, [1,5,6,10], [1,2,3,4])