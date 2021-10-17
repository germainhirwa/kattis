#include <iostream>
using namespace std;

int main()
{
    int n, w;
    cin >> w >> n;
    int ans = 0;
    while (n--) {
        int a,b;
        cin >> a >> b;
        ans += a*b;
    }
    cout << ans/w;
    return 0;
}