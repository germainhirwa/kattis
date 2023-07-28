import java.io.*;
import java.util.*;

public class Apples {
    public static void main(String[] args) throws IOException {
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter writer = new PrintWriter(System.out);
        
        String[] rc = sc.readLine().split(" ");
        int r = Integer.parseInt(rc[0]);
        int c = Integer.parseInt(rc[1]);
        char[][] m = new char[r][c];
        for (int i = 0; i < r; i++) {
            String line = sc.readLine();
            for (int j = 0; j < c; j++) {
                m[i][j] = line.charAt(j);
            }
        }
        
        for (int cn = 0; cn < c; cn++) {
            int offset = 0;
            for (int rn = r - 1; rn >= 0; rn--) {
                if (m[rn][cn] == 'a') {
                    m[rn][cn] = '.';
                    m[rn + offset][cn] = 'a';
                } else if (m[rn][cn] == '.') {
                    offset++;
                } else {
                    offset = 0;
                }
            }
        }
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                sb.append(m[i][j]);
            }
            if (i != r - 1) {
                sb.append("\n");
            }
        }

        writer.println(sb.toString());
        writer.flush();
    }
}