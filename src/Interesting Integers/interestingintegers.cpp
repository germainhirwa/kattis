#include <bits/stdc++.h>
using namespace std;

void solve(long n, long fib[45]) {
    // aFk <= n <= bFk
    // n = aF_(k-2) + bF_(k-1)

    for (int b = 1; b <= n; b++)
        for (int k = 2; k < 45; k++) {
            if (n <= b*fib[k-1]) break;
            
            int a = (n-b*fib[k-1])/fib[k-2];
            if (a > 0 && b >= a && n == a*fib[k-2]+b*fib[k-1]) {
                cout << a << " " << b << endl;
                return;
            }
        }
}

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    long t,n,aa=0,bb=1,temp,fib[45]; // first 45 fibonacci numbers
    for (int i = 0; i < 45; i++) {
        temp = aa;
        aa = bb;
        bb += temp;
        fib[i] = aa;
    }

    cin >> t;
    while (t--) {
        cin >> n;
        solve(n,fib);
    }

    return 0;
}