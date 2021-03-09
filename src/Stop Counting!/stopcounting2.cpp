#include <bits/stdc++.h> 
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    long n,p,i;
    double k=0,s=0,t=0;
    vector<long> cards;
    cin >> n;
    for (i = 0; i < n; i++) {
        cin >> p;
        cards.push_back(p);
    }
    for (i = 0; i < n; i++) {
        s += cards[i];
        k = max(k,s/(i+1));
    }
    for (i = n-1; i >= 0; i--) {
        t += cards[i];
        k = max(k,t/(n-i));
    }

    printf("%.10lf",k);
    return 0;
}