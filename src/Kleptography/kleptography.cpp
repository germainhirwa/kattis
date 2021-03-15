#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int m,n; // n > m
    string a,b;
    cin >> m >> n >> a >> b;
    int ans[n];
    for (int i = n-1; i > -1; i--) {
        if (i >= n-m)
            ans[i] = a[m-n+i]; // fill with the last n letters
        else {
            int step = b[i+m]-ans[i+m];
            if (step < 0)
                step += 26;
            else if (step > 26)
                step -= 26;
            ans[i] = 'a'+step;
        }
    }
    for (int i = 0; i < n; i++)
        cout << (char) ans[i];

    return 0;
}