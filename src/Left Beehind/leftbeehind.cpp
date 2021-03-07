#include <iostream>
using namespace std;

int main() {
    int a,b;
    while (true) {
        cin >> a >> b;
        if (a == 0 && b == 0) {
            break;
        }

        if (a + b == 13) { // never speak again
            cout << "Never speak again." << endl;
        } else if (a < b) { // left beehind, sweet < sour
            cout << "Left beehind." << endl;
        } else if (a == b) { // undecided
            cout << "Undecided." << endl;
        } else {
            cout << "To the convention." << endl;
        }
    }
    return 0;
}