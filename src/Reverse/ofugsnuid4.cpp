// Stack implementation

#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    
    int n,e;
    cin >> n;

    stack<int> s;

    while (n--) {
        cin >> e;
        s.push(e);
    }

    while (s.size()) {
        cout << s.top() << endl;
        s.pop();
    }

    return 0;
}