#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int d,s=0;
    vector<int> v;
    for (int i = 0; i < 9; i++) {
        cin >> d;
        v.push_back(d);
        s += d;
    }
    s -= 100;
    for (int i = 0; i < 9; i++) {
        for (int j = i+1; j < 9; j++) {
            if (v[i] + v[j] == s) {
                for (int k = 0; k < 9; k++) {
                    if (k != i && k != j)
                        cout << v[k] << endl;
                }
                return 0;
            }
        }
    }
    return 0;
}