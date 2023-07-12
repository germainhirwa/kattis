#include <bits/stdc++.h>
using namespace std;
#define REP(i, a) for (int i=0; i<a; i++)
int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    cout.tie(NULL);
    int N=7000, T=2;
    vector<int> v(N), m(N);
    v[0]=m[0]=1;
    char p;
    while (cin >> p) {
        int t = min(T, N)-1;
        if (p=='*') {
            REP(i, t) { v[i]*=5; v[i]+=m[i]; }
            REP(i, t) m[i]*=3;
            REP(i, t) { m[i+1]+=m[i]/10; m[i]%=10; }
        } else if (p=='L') REP(i, t) v[i]*=2;
        else if (p=='R') REP(i, t) { v[i]*=2; v[i]+=m[i]; }
        REP(i, t) { v[i+1]+=v[i]/10; v[i]%=10; }
        T++;
    }
    int pos=N-1;
    while (!v[pos]) pos--;
    for (int i=pos; i>=0; i--) cout << v[i];
    return 0;
}