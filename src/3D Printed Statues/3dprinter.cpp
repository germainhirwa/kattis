#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n,k=1,d=0;
    cin >> n;
    while (k < n) {
        d++;
        k *= 2;
    }
    cout << d+1;

    return 0;
}