#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    
    int w=-1,l=-1,t,x,y,rx,ry,s;
    char d;
    while (true) {
        cin >> w >> l >> t;
        if (w == 0 && l == 0)
            break;

        x = 0;
        y = 0;
        rx = 0;
        ry = 0;
        while (t--) {
            cin >> d >> s;
            if (d == 'u') {
                ry += s;
                y = min(l-1,y+s);
            } else if (d == 'l') {
                rx -= s;
                x = max(0,x-s);
            } else if (d == 'r') {
                rx += s;
                x = min(w-1,x+s);
            } else { // d == 'd'
                ry -= s;
                y = max(0,y-s);
            }
        }

        cout << "Robot thinks " << rx << " " << ry << endl;
        cout << "Actually at " << x << " " << y << endl;
        cout << endl;
    }

    return 0;
}