# 모험가 길드 - 그리디 

import sys
input = sys.stdin.readline

N = int(input())
fears = list(map(int, input().split()))

groups = 0  # 전체 그룹 수
count = 0   # 현재 그룹 내 멤버 수

fears = sorted(fears)
for i in fears:
    count += 1
    if count >= i:
        # 그룹 결성
        groups += 1
        count = 0
    # else면 결성 안되고 한명 더 찾으러 감 -> 다음 i

print(groups)