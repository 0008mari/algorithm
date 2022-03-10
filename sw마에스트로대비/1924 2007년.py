month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

x, y = map(int, input().split())
over = 0
for i in range(1, x):
    over += month[i]
over += y

# print(over)
print(days[over%7])