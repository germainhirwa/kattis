#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int a,b,c;

    while (true) {
        cin >> a >> b >> c;
        if (a == 0 && b == 0 && c == 0)
            return 0;

        cout << (a*a+b*b+c*c == 2*max(a,max(b,c))*max(a,max(b,c)) ? "right" : "wrong") << endl;
    }

    return 0;
}