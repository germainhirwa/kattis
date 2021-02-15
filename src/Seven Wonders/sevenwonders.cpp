#include <iostream>
#include <math.h>
#include <string>
using namespace std;

int main()
{
    int t = 0, g = 0, c = 0;
    string word;
    cin >> word;
    int n = word.length();
    while (n--) {
        switch (word[n]) {
            case 'T':
                t++;
                break;
            case 'G':
                g++;
                break;
            case 'C':
                c++;
                break;
        }
    }
    cout << t*t + g*g + c*c + 7*min(t,min(g,c));
    return 0;
}