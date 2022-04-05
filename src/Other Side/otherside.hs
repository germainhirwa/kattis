solve [] = []
solve (w:s:c:k:r) = (if (s < k || w + c < k || (s == k && w + c <= 2*k) || (w + c == k && s <= 2*k))
    then "YES" else "NO "):solve(r)

slice :: String -> String
slice text = take 3 (drop 1 text)

readInput = (map read) . words
writeOutput = slice . unlines . (map show)

main = interact (writeOutput . solve . readInput)