# 이거...
# 운영체제네 ...

def increaseTurn(turn, max_turn):
    return (turn+1) % max_turn

def solution(food_times, k):
    answer = 0
    turn = 0
    max_turn = len(food_times)
    
    for i in range(max_turn):
        food_times[i] -= k//max_turn

    for i in range(k%max_turn):
        while(food_times[turn]==0):
            turn = increaseTurn(turn, max_turn)
        food_times[turn] -= 1
        turn = increaseTurn(turn, max_turn)
    
    answer = turn+1
    return answer


food_times=[3,1,2]
k=5

print(solution(food_times, k))