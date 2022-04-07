#include<stdio.h>
#include<math.h>
int main()
{
    int n, m,result;
    int x1, y1, r1, x2, y2, r2;
    double distance, r1_r2;
    scanf("%d", &n);
    for (m = 0; m < n; m++)
    {
        scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
        distance = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
        r1_r2 = r1 > r2 ? r1 - r2: r2 - r1;
        if (distance < r1 + r2 && distance > r1_r2) result = 2;
        else if (distance == 0 && r1 == r2) result = -1;
        else if (distance == r1 + r2 || distance == r1_r2) result = 1;
        else result = 0;
        printf("%d\n", result);
    }
}