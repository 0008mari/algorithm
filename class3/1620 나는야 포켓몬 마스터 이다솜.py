# 1620 나는야 포켓몬 마스터 이다솜

import sys
input = sys.stdin.readline

pokedex = dict()

N, M = map(int, input().split())

# 도감 입력
for i in range(1, N+1):
    str = input().rstrip()
    pokedex[i] = str


# 딕셔너리 2개 만들기
pokedexReverse = {v:k for k,v in pokedex.items()}

# 명령 입력
for i in range(M):
    cmd = input().rstrip()
    if cmd.isnumeric():
        print(pokedex[int(cmd)])
    else:
        print(pokedexReverse[cmd])
        

