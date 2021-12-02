def sqrt(x):
    return x**2

li = list(input().split())
li = map(int, li)
print(sum(map(sqrt, li)) % 10)