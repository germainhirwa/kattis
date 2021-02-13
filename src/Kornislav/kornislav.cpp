#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int size = 4;
    int arr[size];
    while (size--) {
        int n;
        cin >> n;
        arr[size] = n;
    }

    sort(arr, arr+4);

    cout << arr[0]*arr[2];
    return 0;
}