#include <iostream>
using namespace std;

int main()
{
    int n;
    while (cin >> n) {
        if (n == -1) {
            break;
        }

        int prev = 0;
        int ans = 0;
        while (n--) {
            int v,t;
            cin >> v >> t;
            ans += v*(t-prev);
            prev = t;
        }
        cout << ans << " miles" << endl;
    }
    return 0;
}