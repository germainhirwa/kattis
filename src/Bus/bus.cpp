#include <iostream>
#include <math.h>

using namespace std;

int main() {
    int t,n;
    cin >> t;
    while (t--) {
        cin >> n;
        printf("%ld\n",pow(2,n)-1);
    }
    return 0;
}