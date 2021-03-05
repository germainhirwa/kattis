#include <iostream>

using namespace std;
int main() {
    int a,b,c,d,e,f,g,h,G,E;
    cin >> a >> b >> c >> d >> e >> f >> g >> h;
    G = a+b+c+d;
    E = e+f+g+h;
    if (G == E) {
        cout << "Tie";
    } else if (G < E) {
        cout << "Emma";
    } else {
        cout << "Gunnar";
    }
    return 0;
}