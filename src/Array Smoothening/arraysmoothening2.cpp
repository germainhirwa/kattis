#include <bits/stdc++.h>
using namespace std;

// Speeds up by 0.01s
const int BUF_SZ = 1 << 16;
char buf[BUF_SZ];
int pos;
int len;
char next_char() {
    if (pos == len) {
        pos = 0;
        len = (int) fread(buf, 1, BUF_SZ, stdin);
        if (!len) {
            return EOF;
        }
    }
    return buf[pos++];
}

int read_int() {
    int x;
    char ch;
    int sgn = 1;
    while (!isdigit(ch = next_char())) {
        if (ch == '-') {
            sgn *= -1;
        }
    }
    x = ch - '0';
    while (isdigit(ch = next_char())) {
        x = x * 10 + (ch - '0');
    }
    return x * sgn;
}

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    cout.tie(NULL);
    
    priority_queue<int> pq;
    unordered_map<int, int> freq;
    int n = read_int(), k = read_int(), x;
    
    while (n--) {
        x = read_int();
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