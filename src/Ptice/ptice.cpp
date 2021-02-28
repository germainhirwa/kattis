#include <iostream>
#include <string>
#include <math.h>
using namespace std;

int main()
{
    int n,a=0,b=0,c=0;
    string s;
    cin >> n >> s;

    for (int i = 0; i < n; i++) {
        switch (i % 3) {
            case 0:
                if (s[i] == 'A') {a++;}
                break;
            case 1:
                if (s[i] == 'B') {a++;}
                break;
            case 2:
                if (s[i] == 'C') {a++;}
                break;
        }

        if (i % 2 == 0 && s[i] == 'B') {
            b++;
        } else if (i % 4 == 1 && s[i] == 'A') {
            b++;
        } else if (i % 4 == 3 && s[i] == 'C') {
            b++;
        }

        switch ((i % 6)/2) {
            case 0:
                if (s[i] == 'C') {c++;}
                break;
            case 1:
                if (s[i] == 'A') {c++;}
                break;
            case 2:
                if (s[i] == 'B') {c++;}
                break;
        }
    }

    int k = max(a,max(b,c));
    cout << k << endl;
    if (a == k) {
        cout << "Adrian" << endl;
    }
    if (b == k) {
        cout << "Bruno" << endl;
    }
    if (c == k) {
        cout << "Goran" << endl;
    }

    return 0;
}