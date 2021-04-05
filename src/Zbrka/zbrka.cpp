#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n, c, MOD = 1000000007;
    cin >> n >> c;

    /*
    f(0,c) = 0
    f(n,0) = 1 (sorted array)
    f(n,c) = sum(f(n-1,i) for i = c,c-1,..,max(c-n+1,0))
    */

    long table[n+1][c+1];

    for (int i = 0; i <= n; i++)
        table[i][0] = 1;

    for (int i = 0; i <= n; i++)
        for (int j = 1; j <= c; j++)
            table[i][j] = 0;

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= c; j++)
            table[i][j] = (MOD + table[i][j-1] + table[i-1][j] - (j >= i ? table[i-1][j-i] : 0)) % MOD;

    cout << table[n][c];

    return 0;
}