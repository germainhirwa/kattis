#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n,p,q,t,k;
    char d;
    cin >> n;
    while (n--) {
        cin >> t >> p >> d >> q;
        vector<int> bin;
        while (p*q != 1) {
            if (p > q) {
                p -= q;
                bin.push_back(1);
            } else {
                q -= p;
                bin.push_back(0);
            }
        }
        bin.push_back(1);
        k = 0;
        for (int i = (int) bin.size()-1; i >= 0; i--) {
            k *= 2;
            k += bin[i];
        }
        cout << t << " " << k << endl;
    }
    return 0;
}