#include <iostream>
#include <string>
using namespace std;

int main()
{
    string msg;
    cin >> msg;
    string left = msg.substr(0,msg.length()/2);
    string right = msg.substr(msg.length()/2,msg.length());
    int ls = 0;
    int rs = 0;
    for (int i = 0; i < msg.length()/2; i++) {
        ls += (int) left[i] - 'A';
        rs += (int) right[i] - 'A';
    }
    for (int i = 0; i < msg.length()/2; i++) {
        left[i]  = (left[i] + ls - 'A') % 26 + 'A';
        right[i]  = (right[i] + rs - 'A') % 26 + 'A';
        left[i] = (left[i] + right[i] - 2*'A') % 26 + 'A';
    }
    cout << left;
    return 0;
}