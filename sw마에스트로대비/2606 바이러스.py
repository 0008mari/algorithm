# 2606 바이러스 

# 이번엔 dfs로 해봄
def dfs(graph, start, visited):
    stack = []
    visited[start] = True
    stack.append(start)
    count = 0
    while stack:
        v = stack.pop()
        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                count += 1
                stack.append(w)
    
    return count


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)

# 입력 끝

visited = [False] * (n+1)
count = dfs(graph, 1, visited)
print(count)
