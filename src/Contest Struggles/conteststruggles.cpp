#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n,k,d,s;
    cin >> n >> k >> d >> s;

    if (0 <= (n*d-k*s) && (n*d-k*s) <= 100*(n-k))
        printf("%.10lf",(double) (n*d-k*s)/(n-k));
    else
        cout << "impossible";

    return 0;
}