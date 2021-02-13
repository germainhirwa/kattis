import java.io.*;

public class InverseFactorial {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        String s = sc.readLine();
        switch (s) {
            case "1":
                writer.print(1);
                writer.flush();
                return;
            case "2":
                writer.print(2);
                writer.flush();
                return;
            case "6":
                writer.print(3);
                writer.flush();
                return;
            case "24":
                writer.print(4);
                writer.flush();
                return;
            case "120":
                writer.print(5);
                writer.flush();
                return;
            case "720": // not necessary but to add triviality
                writer.print(6);
                writer.flush();
                return;
        }
        int digits = s.length();
        int num = 6;
        double init = 4*Math.log10(2) + 2*Math.log10(3) + Math.log10(5);
        while (init < digits) {
            num++;
            init += Math.log10(num);
        }
        writer.print(num-1);
        writer.flush();
    }
}