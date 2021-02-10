#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int m, n;
    cin >> m >> n;
    for (int i = min(m,n)+1; i < max(m,n)+1; i++) {
        cout << i << "\n";
    }
    cout << max(m,n)+1;
    return 0;
}