#include <stdio.h>
#pragma waring (disable: 4996)


int recursion(int result, int goal, int depth);

int main(){
    int a, b;

    scanf("%d %d", &a, &b);
    printf("%d", recursion(a, b, 0) + 1);

    return 0;

}

int recursion(int result, int goal, int depth){
    if (result>goal) return -1;
    else if (result == goal) return depth;

    recursion(result*2, goal, depth+1);
    recursion(result*10+1, goal, depth+1);

}
