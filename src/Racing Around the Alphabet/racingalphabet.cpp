#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n,p,ans,t;
    string s;
    cin >> n;
    getline(cin, s); // skip a line
    while (n--) {
        getline(cin, s);
        if (s[0] == '\'')
            p = 28;
        else if (s[0] == ' ')
            p = 27;
        else
            p = (int) s[0]-64;
        ans = 0;
        t = 1;
        for (int i = 1; i < (int) s.length(); i++) {
            if (s[i] == '\'') {
                ans += min(abs(28-p),28-abs(28-p));
                p = 28;
            } else if (s[i] == ' ') {
                ans += min(abs(27-p),28-abs(27-p));
                p = 27;
            } else { // is an alphabet
                ans += min(abs((int) s[i]-64-p),28-abs((int) s[i]-64-p));
                p = (int) s[i]-64;
            }
            t++;
        }
        printf("%.10lf\n",M_PI*ans/7 + t);
    }

    return 0;
}