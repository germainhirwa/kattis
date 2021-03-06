import java.io.*;
import java.util.*;

public class WeakVertices {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        while (true) {
            int n = Integer.parseInt(sc.readLine());
            if (n == -1) {
                writer.flush();
                return;
            } else if (n < 3) {
                for (int i = 0; i < n; i++) {
                    String dummy = sc.readLine();
                    writer.print(i);
                    writer.print(" ");
                }
                writer.println();
            } else {
                List<Integer> weakList = new ArrayList<Integer>();
                int[][] arr = new int[n][n];
                boolean[] found = new boolean[n];
                for (int i = 0; i < n; i++) {
                    found[i] = false;
                    String[] line = sc.readLine().split(" ");
                    for (int j = 0; j < n; j++) {
                        arr[i][j] = Integer.parseInt(line[j]);
                    }
                }

                // Improving this part somehow gives WA, so I'll just stick to this for now
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        for (int k = 0; k < n; k++) {
                            if (arr[i][j]*arr[i][k]*arr[j][k] == 1) {
                                found[i] = true;
                                found[j] = true;
                                found[k] = true;
                                break;
                            }
                        }
                    }
                    if (!found[i]) {
                        weakList.add(i);
                    }
                }

                for (int i : weakList) {
                    writer.print(i);
                    writer.print(" ");
                }
                writer.println();
            }
        }
    }
}