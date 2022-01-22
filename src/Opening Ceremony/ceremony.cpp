#include <bits/stdc++.h>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    
    int t, u, s = 0, cp = 0;
    vector<int> n;
    cin >> t;
    
    for (int i = 0; i < t; i++) {
        cin >> u;
        n.push_back(u);
    }
    sort(n.begin(), n.end(), greater<int>());
    
    while (t > cp) {
        if (cp < t && t - cp > n[cp]) {
            for (int i = cp; i < t; i++) {
                n[i]--;
            }
            while (n.size() != 0 && n.back() == 0) {
                n.pop_back();
                t--;
            }
        } else {
            cp++;
        }
        s++;
    }
    
    cout << s;

    return 0;
}