#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n,p,q,curr;
    long ans;
    cin >> n >> q;
    vector<int> v,v2;

    while (n--) {
        cin >> p;
        v.push_back(p);
    }

    switch (q) {
        case 1:
            cout << 7;
            break;
        case 2:
            if (v[0] > v[1])
                cout << "Bigger";
            else if (v[0] == v[1])
                cout << "Equal";
            else
                cout << "Smaller";
            break;
        case 3:
            v2 = {v[0],v[1],v[2]};
            sort(v2.begin(),v2.end());
            cout << v2[1];
            break;
        case 4:
            ans = 0;
            for (int i : v)
                ans += i;
            cout << ans;
            break;
        case 5:
            ans = 0;
            for (int i : v)
                ans += (i % 2 == 0 ? i : 0);
            cout << ans;
            break;
        case 6:
            for (int i : v)
                cout << (char) (i % 26 + 'a');
            break;
        case 7:
            set<int> seq;
            curr = 0;
            while (true) {
                curr = v[curr];
                if (curr >= (int) v.size()) {
                    cout << "Out";
                    break;
                } else if (curr == (int) v.size()-1) {
                    cout << "Done";
                    break;
                } else if (seq.find(curr) != seq.end()) {
                    cout << "Cyclic";
                    break;
                } else
                    seq.insert(curr);
            }
            break;
    }

    return 0;
}