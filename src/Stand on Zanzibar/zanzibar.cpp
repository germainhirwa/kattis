#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    while (n--) {
        int x = -1;
        vector<int> data;
        while (x != 0) {
            cin >> x;
            data.push_back(x);
        }
        int ans = 0;
        for (int i = 1; i < data.size(); i++) {
            ans += max(0,data[i]-2*data[i-1]);
        }
        cout << ans << endl;
    }
    return 0;
}