#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    int w,p,x;
    vector<int> walls, res;
    unordered_set <int> dist;
    cin >> w >> p;
    walls.push_back(0);
    for (int i = 0; i < p; i++) {
        cin >> x;
        walls.push_back(x);
    }
    walls.push_back(w);
    for (int i = 0; i < p+2; i++)
        for (int j = i+1; j < p+2; j++)
            dist.insert(walls[j]-walls[i]);

    for (const auto& e: dist)
        res.push_back(e);

    sort(res.begin(),res.end());

    for (const auto& d: res)
        cout << d << " ";
    cout << endl;

    return 0;
}