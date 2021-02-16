#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int min = 1000000000;
    int ans = 0;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        if (x < min) {
            min = x;
            ans = i;
        }
    }
    cout << ans;
    return 0;
}