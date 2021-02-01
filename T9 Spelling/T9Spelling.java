import java.io.*;

public class T9Spelling {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        int n = Integer.parseInt(sc.readLine());
        for (int i = 1; i <= n; i++) {
            String word = sc.readLine();
            String result = "Case #"+i+": ";
            for (int j = 0; j < word.length(); j++) {
                String wk = key(word.charAt(j));
                if (result.charAt(result.length()-1) == wk.charAt(0)) {
                    result += " "+wk;
                } else {
                    result += wk;
                }
            }
            writer.println(result);
        }
        writer.flush();
    }

    static String key(char c) {
        switch (c) {
          case 'a':return ("2");
          case 'b':return ("22");
          case 'c':return ("222");
          case 'd':return ("3");
          case 'e':return ("33");
          case 'f':return ("333");
          case 'g':return ("4");
          case 'h':return ("44");
          case 'i':return ("444");
          case 'j':return ("5");
          case 'k':return ("55");
          case 'l':return ("555");
          case 'm':return ("6");
          case 'n':return ("66");
          case 'o':return ("666");
          case 'p':return ("7");
          case 'q':return ("77");
          case 'r':return ("777");
          case 's':return ("7777");
          case 't':return ("8");
          case 'u':return ("88");
          case 'v':return ("888");
          case 'w':return ("9");
          case 'x':return ("99");
          case 'y':return ("999");
          case 'z':return ("9999");
          case ' ':return ("0");
        }
        return ("");
    }
}