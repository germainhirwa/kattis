#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int x=0,y=0;
    string s;
    cin >> s;
    for (int i = 0; i < (int) s.length(); i++) {
        x *= 2;
        y *= 2;
        if (s[i] == '1' || s[i] == '3')
            x++;
        if (s[i] == '2' || s[i] == '3')
            y++;
    }
    cout << s.length() << " " << x << " " << y;

    return 0;
}