#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    
    string s;
    int p=13,k=13,h=13,t=13;
    set<string> cards;
    cin >> s;
    for (int i = 0; i < (int) s.length()/3; i++) {
        string c = s.substr(3*i,3);

        if (cards.find(c) != cards.end()) {
            cout << "GRESKA";
            return 0;
        }

        cards.insert(c);
        switch (c[0]) {
            case 'P':
                p--;
                break;
            case 'K':
                k--;
                break;
            case 'H':
                h--;
                break;
            case 'T':
                t--;
                break;
        }
    }

    cout << p << " " << k << " " << h << " " << t << endl;

    return 0;
}