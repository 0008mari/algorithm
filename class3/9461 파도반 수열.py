# 9461 파도반 수열

# Padovan sequence

P = [0,1,1,1]


def getPSequence(N):
    if N<len(P):
        return P[N]
    # else
    for i in range(len(P), N+1):
        P.append(P[i-2] + P[i-3])
    return P[N]
    


T = int(input())

for _ in range(T):
    N = int(input())
    print(getPSequence(N))