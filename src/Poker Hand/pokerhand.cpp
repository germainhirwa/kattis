#include <iostream>
#include <string>
using namespace std;

// Trying to avoid map :-D
int main()
{
    int n = 5;
    int arr[13] = {0,0,0,0,0,0,0,0,0,0,0,0,0};
    while (n--) {
        string card;
        cin >> card;
        switch (card[0]) {
            case 'A':
                arr[0]++;
                break;
            case '2':
                arr[1]++;
                break;
            case '3':
                arr[2]++;
                break;
            case '4':
                arr[3]++;
                break;
            case '5':
                arr[4]++;
                break;
            case '6':
                arr[5]++;
                break;
            case '7':
                arr[6]++;
                break;
            case '8':
                arr[7]++;
                break;
            case '9':
                arr[8]++;
                break;
            case 'T':
                arr[9]++;
                break;
            case 'J':
                arr[10]++;
                break;
            case 'Q':
                arr[11]++;
                break;
            case 'K':
                arr[12]++;
                break;
        }
    }
    int ans = 0;
    for (int i = 0; i < 13; i++) {
        if (arr[i] > ans) {
            ans = arr[i];
        }
    }
    cout << ans;
    return 0;
}