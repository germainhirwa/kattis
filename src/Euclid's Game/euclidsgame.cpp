#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    while (true) {
        int a,b;
        cin >> a >> b;
        if (a == 0 && b == 0)
            break;
        
        cout << ((a^b) % 2 == 0 ? "Stan wins" : "Ollie wins") << endl;
    }

    return 0;
}