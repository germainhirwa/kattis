#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int c = 1;
    string n,m;
    while (cin >> n >> m) {
        cout << "Case " << c << ": ";
        if (n.compare("A#") == 0)
            cout << "Bb " << m << endl;
        else if (n.compare("Bb") == 0)
            cout << "A# " << m << endl;
        else if (n.compare("C#") == 0)
            cout << "Db " << m << endl;
        else if (n.compare("Db") == 0)
            cout << "C# " << m << endl;
        else if (n.compare("D#") == 0)
            cout << "Eb " << m << endl;
        else if (n.compare("Eb") == 0)
            cout << "D# " << m << endl;
        else if (n.compare("F#") == 0)
            cout << "Gb " << m << endl;
        else if (n.compare("Gb") == 0)
            cout << "F# " << m << endl;
        else if (n.compare("G#") == 0)
            cout << "Ab " << m << endl;
        else if (n.compare("Ab") == 0)
            cout << "G# " << m << endl;
        else
            cout << "UNIQUE";
        c++;
    }
    return 0;
}