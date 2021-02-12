#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int nums[n];

    for (int i = 0; i < n; i++) {
        int e;
        cin >> e;
        nums[n-1-i] = e;
    }

    for (int j = 0; j < n; j++) {
        cout << nums[j] << endl;
    }

    return 0;
}