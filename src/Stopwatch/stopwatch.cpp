#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int t, p=0, s, v;
    bool start = false;
    cin >> t;
    if (t % 2 == 1) {
        cout << "still running";
        return 0;
    }

    while (t--) {
        cin >> s;
        if (!start) {
            v = s;
            start = true;
        } else {
            p += s-v;
            start = false;
        }
    }

    cout << p;

    return 0;
}