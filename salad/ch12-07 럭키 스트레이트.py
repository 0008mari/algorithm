n = input()
n = list(n)

leftsum, rightsum = 0, 0

for i in range(len(n)//2):
    leftsum += int(n[i])
for i in range(len(n)//2, len(n)):
    rightsum += int(n[i])

if leftsum == rightsum:
    print("LUCKY")
else:
    print("READY")