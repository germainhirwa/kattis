#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n, p = 1;
    bool done = false;
    cin >> n;
    while (!done) {
        if (n % 10 == 0) {
            n /= 10;
        }
        p *= n % 10;
        n /= 10;
        if (n == 0) {
            n = p;
            p = 1;
        }
        if (p < 10)
            done = true;
    }
    cout << n;

    return 0;
}