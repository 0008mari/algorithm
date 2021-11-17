# 1074 Z

rst = 0

def getZNum(N, r, c, znum):
    offset = 2**(N-1)
    # print("offset, znum", offset, znum)
    # print("r c", r, c)
    if offset == 1:
        if r<1 and c==1:
            znum += 1
        elif r==1 and c<1:
            znum += 2
        elif r==1 and c==1:
            znum += 3
        global rst
        rst = znum
        return

    if r<offset and c<offset:
        getZNum(N-1, r, c, znum)
    elif r<offset and c>=offset:
        znum += offset**2
        getZNum(N-1, r, c-offset, znum)
    elif r>=offset and c<offset:
        znum += 2 * offset**2
        getZNum(N-1, r-offset, c, znum)
    else:
        znum += 3 * offset**2
        getZNum(N-1, r-offset, c-offset, znum)
    



# main

N, r, c = map(int, input().split())
a = getZNum(N, r, c, 0)
print(rst)