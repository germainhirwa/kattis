import java.io.*;
import java.util.*;

public class Bijele {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        String[] line = sc.readLine().split(" ");
        int a = Integer.parseInt(line[0]);
        int b = Integer.parseInt(line[1]);
        int c = Integer.parseInt(line[2]);
        int d = Integer.parseInt(line[3]);
        int e = Integer.parseInt(line[4]);
        int f = Integer.parseInt(line[5]);

        writer.print(1-a);
        writer.print(" ");
        writer.print(1-b);
        writer.print(" ");
        writer.print(2-c);
        writer.print(" ");
        writer.print(2-d);
        writer.print(" ");
        writer.print(2-e);
        writer.print(" ");
        writer.print(8-f);

        writer.flush();
    }
}