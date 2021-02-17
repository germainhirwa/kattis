#include <iostream>
#include <math.h>
using namespace std;

int main() {
    int limit, n, t;
    cin >> limit >> n >> t;
    int ans = 1;
    int i;
    bool flag;
    switch (t) {
        case 1:
            for (i = 2; i <= n && ans <= limit; i++) {
                if (ans*i > limit) {
                    break;
                }
                ans *= i;
            }
            flag = i == (n+1);
            break;
        case 2:
            flag = limit >= pow(2,n);
            break;
        case 3:
            flag = limit >= pow(n,4);
            break;
        case 4:
            flag = limit >= pow(n,3);
            break;
        case 5:
            flag = limit >= pow(n,2);
            break;
        case 6:
            flag = limit >= n*log2(n);
            break;
        case 7:
            flag = limit >= n;
            break;
    }
    cout << (flag ? "AC" : "TLE");
    return 0;
}