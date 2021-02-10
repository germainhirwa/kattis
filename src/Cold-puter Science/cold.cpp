#include <iostream>
using namespace std;

int main()
{
    int n;
    int ans = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;
        if (t < 0) {
            ans++;
        }
    }
    cout << ans;
    return 0;
}