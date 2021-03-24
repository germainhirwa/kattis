#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n,m,s;
    while (cin >> n >> m) {
        int stones[m];
        bool wins[n];
        for (int i = 0; i < m; i++) {
            cin >> s;
            stones[i] = s;
            wins[s-1] = true;
        }
        for (int i = 0; i < n; i++) { // for every number of starting stones i+1
            bool found = false;
            for (int j = 0; j < m; j++) {
                if (stones[j] == i+1) {
                    found = true;
                    break;
                }
            }
            if (!found) { // if we haven't assign it to a position
                wins[i] = false;
                for (int t : stones) {
                    if (i >= t)
                        wins[i] |= !wins[i-t];
                }
            }
        }

        cout << (wins[n-1] ? "Stan wins" : "Ollie wins") << endl;
    }

    return 0;
}