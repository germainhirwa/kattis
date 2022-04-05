fun main(args: Array<String>) {
    var (w, s, c, k) = readLine()!!.trim().split("\\s+".toRegex()).map (String::toInt)
    if (s < k || w + c < k || (s == k && w + c <= 2*k) || (w + c == k && s <= 2*k))
        println("YES");
    else
        println("NO");
}