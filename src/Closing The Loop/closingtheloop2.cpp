#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int s;
        cin >> s;
        vector<int> b, r;
        if (s == 1) {
            string dummy;
            cin >> dummy;
            cout << "Case #" << i+1 << ": 0" << endl;
            continue;
        }
        
        while (s--) {
            string seg;
            int new_seg;
            cin >> seg;
            stringstream ss;
            ss << seg;
            ss >> new_seg;

            if (seg.back() == 'R') {
                r.push_back(new_seg);
            } else {
                b.push_back(new_seg);
            }
        }

        if (r.size() == 0 || b.size() == 0) {
            cout << "Case #" << i+1 << ": 0" << endl;
            continue;
        }

        sort(b.rbegin(),b.rend());
        sort(r.rbegin(),r.rend());

        int ans = 0;
        int minsize = min(r.size(),b.size());
        for (int i = 0; i < minsize; i++) {
            ans += r[i]+b[i]-2;
        }
        cout << "Case #" << i+1 << ": " << ans << endl;
    }

    return 0;
}