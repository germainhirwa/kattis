#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n,a=0,b=0;
    cin >> n;

    int num[n];
    for (int i = 0; i < n; i++)
        cin >> num[i];

    sort(num,num+n,greater<int>());
    for (int i = 0; i < n; i++)
        if (i % 2 == 1)
            b += num[i];
        else
            a += num[i];

    cout << a << " " << b;

    return 0;
}