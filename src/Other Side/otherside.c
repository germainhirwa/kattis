#include <stdio.h>

int main() {
    int w, s, c, k;
    if (scanf("%d %d %d %d", &w, &s, &c, &k) != 0) {
        if (s < k || w + c < k || (s == k && w + c <= 2*k) || (w + c == k && s <= 2*k))
            printf("YES");
        else
            printf("NO");
    }
    
    return 0;
}