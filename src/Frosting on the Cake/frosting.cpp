#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n;
    long c;
    cin >> n;
    long a[3], b[3];

    for (int i = 0; i < 3; i++) {
        a[i] = 0;
        b[i] = 0;
    }

    for (int i = 0; i < n; i++) {
        cin >> c;
        a[i%3] += c;
    }

    for (int i = 0; i < n; i++) {
        cin >> c;
        b[i%3] += c;
    }

    cout << a[1]*b[0] + a[2]*b[2] + a[0]*b[1] << " ";
    cout << a[2]*b[0] + a[0]*b[2] + a[1]*b[1] << " ";
    cout << a[0]*b[0] + a[1]*b[2] + a[2]*b[1];

    return 0;
}