#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int t, l;
    string n;

    cin >> t;
    while (t--) {
        cin >> n;
        l = 0;
        for (int i = 1; i <= (int) n.size(); i++)
            l += (i % 2 == 1 ? n[n.size()-i] - 48 : (2*(n[n.size()-i] - 48) == 18 ? 9 : 2*(n[n.size()-i] - 48) % 9));

        cout << (l % 10 == 0 ? "PASS" : "FAIL") << endl;
    }

    return 0;
}