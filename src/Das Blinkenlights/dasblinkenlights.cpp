#include <bits/stdc++.h>
using namespace std;

int lcm (int a, int b) {
    int A = a, B = b;

    while (b) {
        int temp = a;
        a = b;
        b = temp % b;
    }

    return A*B/a;
}

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int a,b,c;
    cin >> a >> b >> c;
    cout << (lcm(a,b) <= c ? "yes" : "no");

    return 0;
}