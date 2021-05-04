#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int t,n,k,p,q;
    cin >> t;
    while (t--) {
        cin >> n >> k;
        vector<int> bin;
        while (k != 1) {
            bin.push_back(k % 2);
            k /= 2;
        }

        p = 1;
        q = 1;

        for (int i = bin.size()-1; i >= 0; i--)
            if (bin[i] == 0)
                q += p;
            else
                p += q;
        
        printf("%d %d/%d\n",n,p,q);
    }

    return 0;
}