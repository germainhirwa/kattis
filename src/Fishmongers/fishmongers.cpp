#include <bits/stdc++.h>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    
    long n, m, a, b;
    vector<long> w, p(100001), g;
    for (int i = 0; i < 100001; i++) {
        p[i] = 0;
    }
    
    cin >> n >> m;
    while (n-- > 0) {
        cin >> a;
        w.push_back(a);
    }
    while (m-- > 0) {
        cin >> a >> b;
        p[b] += a;
    }
    sort(w.begin(), w.end(), greater<int>());
    for (int i = 100000; i >= 0; i--) {
        if (p[i] != 0) {
            g.push_back(i);
        }
    }
    
    long long ans = 0;
    int pos_w = 0, pos_g = 0, tmp, price, qty;
    while (pos_w < (int) w.size() && pos_g < (int) g.size()) {
        price = g[pos_g];
        qty = p[price];
        tmp = pos_w;
        while (pos_w < min((int) w.size(), tmp + qty)) {
            ans += price * w[pos_w];
            pos_w++;
        }
        pos_g++;
    }
    
    cout << ans;

    return 0;
}