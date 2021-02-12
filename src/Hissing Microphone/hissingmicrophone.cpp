#include <iostream>
#include <string>
using namespace std;

int main()
{
    string input;
    cin >> input;
    size_t found = input.find("ss");
    if (found != string::npos) {
        cout << "hiss";
    } else {
        cout << "no hiss";
    }
    return 0;
}