#include <bits/stdc++.h>
using namespace std;

bool solve(int n) {
    for (int a = 1; a <= 20; a++) {
        for (int b = 0; b <= 3; b++) {
            for (int c = 1; c <= 20; c++) {
                for (int d = 0; d <= 3; d++) {
                    for (int e = 1; e <= 20; e++) {
                        for (int f = 0; f <= 3; f++) {
                            if (a*b+c*d+e*f==n) {
                                switch (b) {
                                    case 1:
                                        cout  << "single " << a << endl;
                                        break;
                                    case 2:
                                        cout  << "double " << a << endl;
                                        break;
                                    case 3:
                                        cout  << "triple " << a << endl;
                                        break;
                                }
                                switch (d) {
                                    case 1:
                                        cout  << "single " << c << endl;
                                        break;
                                    case 2:
                                        cout  << "double " << c << endl;
                                        break;
                                    case 3:
                                        cout  << "triple " << c << endl;
                                        break;
                                }
                                switch (f) {
                                    case 1:
                                        cout  << "single " << e << endl;
                                        break;
                                    case 2:
                                        cout  << "double " << e << endl;
                                        break;
                                    case 3:
                                        cout  << "triple " << e << endl;
                                        break;
                                }
                                return true;
                            }
                        }
                    }
                }
            }
        }
    }
    return false;
}

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n;
    cin >> n;
    
    if (!solve(n))
        cout << "impossible";
    
    return 0;
}