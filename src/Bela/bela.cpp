#include <iostream>
#include <string>
using namespace std;

int main()
{
    int n, ans = 0;
    string suit;
    cin >> n >> suit;
    for (int i = 0; i < 4*n; i++) {
        string card;
        cin >> card;
        if (card.substr(1,2).compare(suit) == 0) {
            if (card.substr(0,1).compare("A") == 0) {
                ans += 11;
            } else if (card.substr(0,1).compare("K") == 0) {
                ans += 4;
            } else if (card.substr(0,1).compare("Q") == 0) {
                ans += 3;
            } else if (card.substr(0,1).compare("J") == 0) {
                ans += 20;
            } else if (card.substr(0,1).compare("T") == 0) {
                ans += 10;
            } else if (card.substr(0,1).compare("9") == 0) {
                ans += 14;
            }
        } else {
            if (card.substr(0,1).compare("A") == 0) {
                ans += 11;
            } else if (card.substr(0,1).compare("K") == 0) {
                ans += 4;
            } else if (card.substr(0,1).compare("Q") == 0) {
                ans += 3;
            } else if (card.substr(0,1).compare("J") == 0) {
                ans += 2;
            } else if (card.substr(0,1).compare("T") == 0) {
                ans += 10;
            }
        }
    }
    cout << ans;
    return 0;
}