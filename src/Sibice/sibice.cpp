#include <iostream>
using namespace std;

int main()
{
    int n, w, h;
    cin >> n >> w >> h;
    for (int i = 0; i < n; i++) {
        int l;
        cin >> l;
        cout << ((l*l <= w*w + h*h) ? "DA" : "NE") << endl;
    }
    return 0;
}