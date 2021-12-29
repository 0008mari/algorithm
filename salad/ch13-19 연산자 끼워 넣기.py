from sys import stdin
input = stdin.readline



n = int(input())
nums = list(map(int, input().split()))
operands = list(map(int, input().split()))


# dfs를 이용해서 완전탐색 ㅅㄱㄴ이네.. 
MIN = 100000000
MAX = -100000000

def dfs(depth, total, plus, minus, mul, div):
    global MIN, MAX
    if depth == n:
        MAX = max(total, MAX)
        MIN = min(total, MIN)
        return
        # 탐색 완료
    
    if plus:
        dfs(depth+1, total+nums[depth], plus-1, minus, mul, div)
    if minus:
        dfs(depth+1, total-nums[depth], plus, minus-1, mul, div)       
    if mul:
        dfs(depth+1, total*nums[depth], plus, minus, mul-1, div)
    if div:
        dfs(depth+1, int(total/nums[depth]), plus, minus, mul, div-1)
        

dfs(1, nums[0], operands[0], operands[1], operands[2], operands[3])
print(MAX)
print(MIN)