import java.io.*;

public class Billiard {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        while (true) {
            String line = sc.readLine();
            
            if (line.equals("0 0 0 0 0")) {
                writer.flush();
                return;
            }
            
            String[] nums = line.split(" ");
            int a = Integer.parseInt(nums[0]);
            int b = Integer.parseInt(nums[1]);
            int s = Integer.parseInt(nums[2]);
            int m = Integer.parseInt(nums[3]);
            int n = Integer.parseInt(nums[4]);
            double angle = Math.atan(b*n*1.0/(a*m))*180/Math.PI;
            double velocity = Math.sqrt(Math.pow(a*m,2)+Math.pow(b*n,2))/s;

            writer.printf("%.2f",Math.round(angle*100)/100.0);
            writer.print(" ");
            writer.printf("%.2f",Math.round(velocity*100)/100.0);
            writer.println();
        }
    }
}