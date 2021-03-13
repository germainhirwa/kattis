#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n;
    cin >> n;
    string prev = "-";
    bool dec = true, inc = true;
    while (n--) {
        string p;
        cin >> p;
        if (prev.compare("-") == 0)
            prev = p; // filler
        else if (p.compare(prev) > 0)
            dec = false;
        else if (p.compare(prev) < 0)
            inc = false;
        prev = p;
    }
    if (dec)
        cout << "DECREASING";
    else if (inc)
        cout << "INCREASING";
    else
        cout << "NEITHER";

    return 0;
}