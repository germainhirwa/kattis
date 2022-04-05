using System;

public class Program {
    public static void Main() {
        string[] split = Console.ReadLine().Split(new char[] { ' ' }, StringSplitOptions.None);
        long w = Int64.Parse(split[0]), s = Int64.Parse(split[1]), c = Int64.Parse(split[2]), k = Int64.Parse(split[3]);
        if (s < k || w + c < k || (s == k && w + c <= 2*k) || (w + c == k && s <= 2*k))
            Console.WriteLine("YES");
        else
            Console.WriteLine("NO");
    }
}