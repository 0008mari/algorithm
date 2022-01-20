# 못생긴 수

# sol 1. n번째 못생긴 수가
# 나올 때까지 1부터 모든 수를
# 2, 3, 5 나눠 확인한다.
# ---> 시간초과

# 못생긴 수의 기본: 1
# 여기에 2, 3, 5 곱한 결과도 못생긴 수가 된다.

n = int(input())
uglys = [1]   # 못생긴 수 리스트.
factors = [2, 3, 5]

for _ in range(n):
    tmp = []
    for ugly in uglys:
        for factor in factors:
            tmp.append(ugly * factor)
    # uglys 리스트의 목록과 factor 곱한 값을 tmp로
    uglys += tmp   # list 합치기
    uglys = sorted(list(set(uglys)))   # 중복제거 후 다시 list로

print(uglys[n-1])