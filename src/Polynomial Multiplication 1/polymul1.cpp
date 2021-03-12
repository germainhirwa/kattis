#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n;
    cin >> n;
    while (n--) {
        int d1, d2, p;
        vector<int> coefs1, coefs2;
        cin >> d1;
        for (int d = 0; d <= d1; d++) {
            cin >> p;
            coefs1.push_back(p);
        }
        cin >> d2;
        for (int d = 0; d <= d2; d++) {
            cin >> p;
            coefs2.push_back(p);
        }
        vector<int> result(d1+d2+1,0);
        for (int i = 0; i <= d1; i++)
            for (int j = 0; j <= d2; j++)
                result[i+j] += coefs1[i]*coefs2[j];

        cout << d1+d2 << endl;
        for (int c : result)
            cout << c << " ";
        cout << endl;
    }

    return 0;
}