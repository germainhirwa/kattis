import java.io.*;

public class T9Spelling2 {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        int n = Integer.parseInt(sc.readLine());

        String[] keys = new String[128];
        keys['a'] = "2";
        keys['b'] = "22";
        keys['c'] = "222";
        keys['d'] = "3";
        keys['e'] = "33";
        keys['f'] = "333";
        keys['g'] = "4";
        keys['h'] = "44";
        keys['i'] = "444";
        keys['j'] = "5";
        keys['k'] = "55";
        keys['l'] = "555";
        keys['m'] = "6";
        keys['n'] = "66";
        keys['o'] = "666";
        keys['p'] = "7";
        keys['q'] = "77";
        keys['r'] = "777";
        keys['s'] = "7777";
        keys['t'] = "8";
        keys['u'] = "88";
        keys['v'] = "888";
        keys['w'] = "9";
        keys['x'] = "99";
        keys['y'] = "999";
        keys['z'] = "9999";
        keys[' '] = "0";

        for (int i = 1; i <= n; i++) {
            String word = sc.readLine();
            String previous = " ";
            writer.print("Case #"+i+": ");
            for (int j = 0; j < word.length(); j++) {
                String wk = keys[word.charAt(j)];
                if (previous.equals(wk.substring(0,1))) {
                    writer.print(" "+wk);
                } else {
                    writer.print(wk);
                }
                previous = wk.substring(0,1);
            }
            writer.println();
        }
        writer.flush();
    }
}