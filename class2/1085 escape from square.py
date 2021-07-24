x, y, w, h = map(int, input().split())

list = [x, y]
list.append(h-y)
list.append(w-x)

print(min(list))