import java.io.*;

public class ABC {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        String[] nums = sc.readLine().split(" ");
        int n1 = Integer.parseInt(nums[0]);
        int n2 = Integer.parseInt(nums[1]);
        int n3 = Integer.parseInt(nums[2]);
        int a = Math.min(n1,Math.min(n2,n3));
        int c = Math.max(n1,Math.max(n2,n3));
        int b;
        if (n1 == a || n1 == c) {
            if (n2 == a || n2 == c) {
                b = n3;
            } else {
                b = n2;
            }
        } else {
            b = n1;
        }

        String abc = sc.readLine();

        if (abc.equals("ABC")) {
            writer.print(a);
            writer.print(" ");
            writer.print(b);
            writer.print(" ");
            writer.print(c);
        } else if (abc.equals("ACB")) {
            writer.print(a);
            writer.print(" ");
            writer.print(c);
            writer.print(" ");
            writer.print(b);
        } else if (abc.equals("BAC")) {
            writer.print(b);
            writer.print(" ");
            writer.print(a);
            writer.print(" ");
            writer.print(c);
        } else if (abc.equals("BCA")) {
            writer.print(b);
            writer.print(" ");
            writer.print(c);
            writer.print(" ");
            writer.print(a);
        } else if (abc.equals("CAB")) {
            writer.print(c);
            writer.print(" ");
            writer.print(a);
            writer.print(" ");
            writer.print(b);
        } else {
            writer.print(c);
            writer.print(" ");
            writer.print(b);
            writer.print(" ");
            writer.print(a);
        }

        writer.flush();
    }
}