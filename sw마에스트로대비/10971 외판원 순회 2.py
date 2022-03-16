# 브루트포스
# 모든 순열에 대해 cost 계산하여 min 값을 꺼낸다.

from itertools import permutations
import sys
input = sys.stdin.readline

# get next permutation
# ... for every permutation 경우의 수

# main

n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))

perms = permutations(range(n))
# [0,1,...,n-1]에 대해 순열 생성
# 각 원소는 (0,1,2,3) 이런거임
# 이게 각 노드에 대한 방문 순서가 됨.

ret = sys.maxsize

for perm in perms:
    if graph[perm[-1]][perm[0]] == 0:
        continue    # 불가능한노드 컷
    cost = 0
    flag = True
    for i in range(n-1):
        # 각 노드 연결에 대해 가능한지 체크, 코스트 체크
        v = perm[i]
        w = perm[i+1]
        if graph[v][w] == 0:
            flag = False
            break
        cost += graph[v][w]
        if cost >= ret:
            # 현재 최소값보다 커지면 버림
            flag = False
            break
    if flag == False:
        continue # 버림
    cost += graph[perm[-1]][perm[0]]
    ret = min(ret, cost)

print(ret)