#include <bits/stdc++.h>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n, m;
    vector<int> v, v2;
    cin >> n;
    while (n-- > 0) {
        cin >> m;
        v.push_back(m);
    }

    m = 0;
    for (int i = 0; i < v.size(); i++) {
        if (v[i] > m) {
            v2.push_back(v[i]);
            m = v[i];
        }
    }

    cout << v2.size() << "\n";
    for (int i = 0; i < v2.size() - 1; i++) {
        cout << v2[i] << " ";
    }
    cout << v2[v2.size() - 1];

    return 0;
}