#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int t,r,c;
    string row;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Test " << i << endl;
        cin >> r >> c;
        char map[r][c];
        for (int j = 0; j < r; j++) {
            cin >> row;
            for (int k = 0; k < c; k++)
                map[r-1-j][c-1-k] = row[k];
        }

        for (int j = 0; j < r; j++) {
            for (int k = 0; k < c; k++)
                cout << map[j][k];
            cout << endl;
        }
    }

    return 0;
}