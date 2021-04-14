#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int N,P=1;
    string m;
    cin >> N >> m;

    for (int i = 0; i < m.size(); i++)
        if (m[i] == 'L')
            P *= 2;
        else
            P = 2*P+1;

    cout << (int) pow(2,N+1)-P;

    return 0;
}