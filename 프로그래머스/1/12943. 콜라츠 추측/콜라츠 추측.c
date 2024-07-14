#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int num) {
    int answer = 0;
    long long lnum = (long long) num;
    if (lnum == 1) return answer;
    while (answer < 501) {
        answer++;
        if (lnum % 2 == 0) {
            lnum = lnum / 2;
        } else {
            lnum = lnum * 3 + 1;
        }
        if (lnum == 1)
            return answer;
    }
    return -1;
}