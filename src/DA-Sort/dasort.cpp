#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int t,c,s,p,k;
    cin >> t;
    while (t--) {
        cin >> c >> s;
        vector<int> unsorted, sorted;
        
        for (int i = 0; i < s; i++) {
            cin >> p;
            unsorted.push_back(p);
            sorted.push_back(p);
        }

        sort(sorted.begin(), sorted.end());
        k = 0;
        for (int i = 0; i < s; i++)
            if (sorted[k] == unsorted[i])
                k++;
        
        cout << c << " " << s-k << endl;
    }

    return 0;
}