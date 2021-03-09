#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    
    long t,n,e,d,i,p;
    cin >> t;
    while(t--) {
        cin >> n >> e;
        i = 2;
        while (i*i <= n) {
            if (n % i == 0) {
                n /= i;
                break;
            } else {
                i++;
            }
        }
        p = (n-1)*(i-1); // totient
        d = 1;
        while (d*e % p != 1) {
            d++;
        }
        cout << d << endl;
    }
    return 0;
}