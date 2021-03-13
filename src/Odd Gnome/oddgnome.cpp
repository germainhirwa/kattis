#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n,k,p=-1,c;
    cin >> n;
    while (n--) {
        cin >> k;
        bool found = false;
        for (int i = 1; i <= k; i++) {
            cin >> c;
            if (!found && p != -1 && c-p != 1) {
                cout << i << endl;
                found = true;
            }
            p = c;
        }
        p = -1;
    }
    return 0;
}