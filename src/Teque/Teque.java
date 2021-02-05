import java.io.*;
import java.util.*;

public class Teque {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int n = Integer.parseInt(sc.readLine());
        List<String> teque = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            String[] command = sc.readLine().split(" ");
            switch (command[0]) {
                case "get":
                    writer.println(teque.get(Integer.parseInt(command[1])));
                    break;
                case "push_front":
                    teque.add(0,command[1]);
                    break;
                case "push_back":
                    teque.add(command[1]);
                    break;
                case "push_middle":
                    teque.add((teque.size()+1)/2,command[1]);
                    break;
            }
        }
        
        writer.flush();
    }
}