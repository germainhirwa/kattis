#include <iostream>
#include <string>
using namespace std;

int main()
{
    string a;
    string b;
    cin >> a >> b;

    cout << (a.length() < b.length() ? "no" : "go");
    return 0;
}