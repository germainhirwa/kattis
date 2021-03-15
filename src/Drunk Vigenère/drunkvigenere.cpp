#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    
    string a,b;
    cin >> a >> b;
    for (int i = 0; i < (int) a.length(); i++) {
        if (i % 2 == 0) {
            int k = a[i]-b[i];
            if (k < 0)
                k += 26;
            cout << (char) (k+'A');
        } else
            cout << (char) ((a[i]+b[i])%26+'A');
    }

    return 0;
}