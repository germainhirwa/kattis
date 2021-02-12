#include <iostream>
using namespace std;

int main()
{
    int n;
    double ans = 0;
    int count = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        if (x >= 0) {
            ans += x;
            count++;
        }
    }
    printf("%lf",ans/count);
    return 0;
}