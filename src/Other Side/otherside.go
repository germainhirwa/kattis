package main

import (
    "fmt"
    "io"
)

func main() {
    var w, s, c, k int64

    for {
        _, err := fmt.Scanf("%d%d%d%d", &w, &s, &c, &k)
        if err == io.EOF {
            break
        }

        if (s < k || w + c < k || (s == k && w + c <= 2*k) || (w + c == k && s <= 2*k)) {
            fmt.Printf("YES");
        } else {
            fmt.Printf("NO");
        }
    }
}