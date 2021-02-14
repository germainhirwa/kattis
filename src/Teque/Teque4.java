import java.io.*;
import java.util.*;

public class Teque4 {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int n = Integer.parseInt(sc.readLine());
        Map<Integer,Integer> tequeLeft = new HashMap<Integer,Integer>();
        Map<Integer,Integer> tequeRight = new HashMap<Integer,Integer>();
        int minLeft = 0, maxLeft = 1, minRight = -1, maxRight = 0, leftSize = 0, rightSize = 0;
        
        for (int i = 0; i < n; i++) {
            String[] command = sc.readLine().split(" ");
            switch (command[0]) {
                case "get":
                    int idx = Integer.parseInt(command[1]);
                    if (idx >= leftSize) {
                        writer.println(tequeRight.get(idx-leftSize+minRight+1));
                    } else {
                        writer.println(tequeLeft.get(idx+minLeft+1));
                    }
                    break;
                case "push_front":
                    tequeLeft.put(minLeft,Integer.parseInt(command[1]));
                    leftSize++;
                    minLeft--;
                    break;
                case "push_back":
                    tequeRight.put(maxRight,Integer.parseInt(command[1]));
                    rightSize++;
                    maxRight++;
                    break;
                case "push_middle":
                    tequeLeft.put(maxLeft,Integer.parseInt(command[1]));
                    leftSize++;
                    maxLeft++;
                    break;
            }
            if (!command[0].equals("get")) {
                if (leftSize > rightSize+1) { // move from left
                    tequeRight.put(minRight,tequeLeft.remove(maxLeft-1));
                    leftSize--;
                    rightSize++;
                    minRight--;
                    if (leftSize == 0) {
                        minLeft++;
                    } else {
                        maxLeft--;
                    }
                } else if (rightSize >= leftSize+1) { // move from right
                    tequeLeft.put(maxLeft,tequeRight.remove(minRight+1));
                    leftSize++;
                    rightSize--;
                    maxLeft++;
                    if (rightSize == 0) {
                        maxRight--;
                    } else {
                        minRight++;
                    }
                }
            }
        }
        writer.flush();
    }
}