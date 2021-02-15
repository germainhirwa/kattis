#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>
using namespace std;

int main()
{
    int n;
    cin >> n;

    while (n--) {
        string p;
        cin >> p;
        if (p.compare("P=NP")==0) {
            cout << "skipped" << endl;
        } else {
            stringstream ss(p);
            int a,b;
            char ch;
            ss >> a >> ch >> b;
            cout << a+b << endl;
        }
    }

    return 0;
}