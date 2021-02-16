#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    bool flag = true;
    for (int i = 0; i < 5; i++) {
        string x;
        cin >> x;
        if (x.find("FBI") != string::npos) {
            cout << i+1 << " ";
            flag = false;
        }
    }
    if (flag) {
        cout << "HE GOT AWAY!";
    }
    return 0;
}