#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    string s;
    cin >> s;
    cout << (s.substr(0,3).compare("555") == 0 ? 1 : 0);
    return 0;
}