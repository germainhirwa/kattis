#include <iostream>
#include <string>
using namespace std;

int main()
{
    string month, date;
    string str1 ("OCT 31");
    string str2 ("DEC 25");

    cin >> month >> date;
    string md = month + " " + date;
    if (md.compare(str1) == 0 || md.compare(str2) == 0)
        cout << "yup";
    else
        cout << "nope";
    return 0;
}