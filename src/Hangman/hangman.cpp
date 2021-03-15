#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    string s,a;
    cin >> s >> a;
    set<char> g;
    int f = 0, t = 0;

    for (int i = 0; i < (int) s.length(); i++) {
        g.insert(s[i]);
    }

    for (int i = 0; i < 26; i++) {
        if (g.find(a[i]) != g.end())
            t++;
        else
            f++;
        
        if (f == 10 || t == g.size())
            break;
    }

    cout << (f < 10 ? "WIN" : "LOSE");

    return 0;
}