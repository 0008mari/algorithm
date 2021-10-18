# 2292 벌집

# 껍질만 결정하면 알 수 있어씀 ...

layer = 0

N = int(input())
i = 0 # 6의배수

N -= 1
layer += 1

while (N > 0):
    i += 6
    N -= i
    layer += 1

print(layer)
