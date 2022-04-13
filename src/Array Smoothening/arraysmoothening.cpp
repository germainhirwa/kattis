#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    cout.tie(NULL);
    
    priority_queue<int> pq;
    unordered_map<int, int> freq;
    int n, k, x;
    cin >> n >> k;
    
    while (n--) {
        cin >> x;
        if (freq.find(x) == freq.end())
            freq[x] = 1;
        else
            freq[x]++;
    }

    for (auto kv : freq)
        pq.push(kv.second);

    while (k--) {
        pq.push(pq.top() - 1);
        pq.pop();
    }
    cout << pq.top();

    return 0;
}