// Stack implementation

#include <iostream>
#include <stack>
using namespace std;

int main()
{
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