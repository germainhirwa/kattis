#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    double ans = 0;
    int prev1 = 0;
    double prev2 = 0;
    for (int i = 0; i < n; i++) {
        int t;
        double v;
        cin >> t >> v;
        if (i) {
            ans += (t-prev1) * (v+prev2) / 2000;
        }
        prev1 = t;
        prev2 = v;
    }
    printf("%lf", ans);
    return 0;
}